#!/usr/bin/env python
# coding: utf-8
"""
Clean MTP level 20 training on H2O dataset.

This run fixes the old naming/level mismatch:
old folder new_datasets/water/mtp had job/model names with mtp20,
but the actual MTP constructor used level=16.

This script must be run only through SLURM sbatch on a compute node.
Do not run this script manually on login/guest node.
"""

import csv
import json
import os
import socket
from datetime import datetime

import numpy as np
from mpi4py import MPI
from mlip_4 import LossFunction, RadialBasisCinf, MTP, Trainer


def parse_errors_table(errors_obj):
    """
    Parse mlip_4 calc_errors() text.

    Expected format:
    Errors (MAE, RMSE, MAXAE)
    Energy      = ...
    Energy/Atom = ...
    Forces      = ...

    Returns:
    - Energy/Atom in eV/atom
    - Forces in eV/A
    """
    text = str(errors_obj)
    parsed = {}

    for line in text.splitlines():
        if "=" not in line:
            continue

        key, rhs = line.split("=", 1)
        key = key.strip()
        vals = rhs.replace(",", " ").split()

        if len(vals) < 3:
            continue

        try:
            mae, rmse, maxae = map(float, vals[:3])
        except ValueError:
            continue

        parsed[key] = {
            "mae": mae,
            "rmse": rmse,
            "maxae": maxae,
        }

    required = ["Energy/Atom", "Forces"]
    missing = [key for key in required if key not in parsed]
    if missing:
        raise RuntimeError(
            f"Could not parse required error rows {missing}. Full errors text:\n{text}"
        )

    return parsed


def numeric_metrics_from_errors(errors_obj):
    table = parse_errors_table(errors_obj)

    return {
        "energy": {
            "mae_meV_atom": 1000.0 * table["Energy/Atom"]["mae"],
            "rmse_meV_atom": 1000.0 * table["Energy/Atom"]["rmse"],
            "maxae_meV_atom": 1000.0 * table["Energy/Atom"]["maxae"],
            "units": "meV/atom",
        },
        "forces": {
            "mae_meV_A": 1000.0 * table["Forces"]["mae"],
            "rmse_meV_A": 1000.0 * table["Forces"]["rmse"],
            "maxae_meV_A": 1000.0 * table["Forces"]["maxae"],
            "units": "meV/Å",
        },
    }


def write_metrics_csv(path, metrics):
    rows = []

    for split in ["train", "valid"]:
        rows.append({
            "model_label": "MTP-20",
            "dataset": "water_H2O",
            "split": split,
            "metric": "energy",
            "mae": metrics["metrics"][split]["energy"]["mae_meV_atom"],
            "rmse": metrics["metrics"][split]["energy"]["rmse_meV_atom"],
            "units": "meV/atom",
            "level": metrics["level"],
            "n_params": metrics["n_params"],
        })

        rows.append({
            "model_label": "MTP-20",
            "dataset": "water_H2O",
            "split": split,
            "metric": "forces",
            "mae": metrics["metrics"][split]["forces"]["mae_meV_A"],
            "rmse": metrics["metrics"][split]["forces"]["rmse_meV_A"],
            "units": "meV/Å",
            "level": metrics["level"],
            "n_params": metrics["n_params"],
        })

    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "model_label",
                "dataset",
                "split",
                "metric",
                "mae",
                "rmse",
                "units",
                "level",
                "n_params",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


species_order = [1, 8]  # H, O

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

BASE = "~/coursework/new_datasets"
TRAIN_DB = f"{BASE}/water/convert/train_H2O.json"
VALID_DB = f"{BASE}/water/convert/valid_H2O.json"

OUT_DIR = f"{BASE}/water/mtp_clean20_20260508"
MODEL_PATH = f"{OUT_DIR}/mtp20_trained.json"
METRICS_JSON_PATH = f"{OUT_DIR}/metrics_20_clean.json"
METRICS_CSV_PATH = f"{OUT_DIR}/metrics_20_clean.csv"

if rank == 0:
    os.makedirs(OUT_DIR, exist_ok=True)

train_bytes = b""
if rank == 0:
    with open(TRAIN_DB, "rb") as f:
        train_bytes = f.read()
train_bytes = comm.bcast(train_bytes, root=0)
loss_train = LossFunction.from_json_bytes(train_bytes, True)

valid_bytes = b""
if rank == 0:
    with open(VALID_DB, "rb") as f:
        valid_bytes = f.read()
valid_bytes = comm.bcast(valid_bytes, root=0)
loss_valid = LossFunction.from_json_bytes(valid_bytes, True)

pot_bytes = b""
if rank == 0:
    np.random.seed(42)
    rb = RadialBasisCinf(size=8, min_dist=1.0, cutoff=5.0)
    pot = MTP(rb, species_order, level=20, jit=True)
    pot.params[:] = np.random.uniform(low=-1e-3, high=1e-3, size=len(pot.params))
    pot_bytes = pot.to_json_bytes()

    print(f"MTP level 20: {len(pot.params)} parameters, {len(species_order)} species")
    print(f"TRAIN_DB: {TRAIN_DB}")
    print(f"VALID_DB: {VALID_DB}")
    print(f"OUT_DIR: {OUT_DIR}")

pot_bytes = comm.bcast(pot_bytes, root=0)
pot = MTP.from_json_bytes(pot_bytes)

trainer = Trainer(loss_train)
train_result = trainer.train(pot, max_iter_count=2000)

loss_train.attach_pot(pot)
loss_train.calc()
train_errors = loss_train.calc_errors()

loss_valid.attach_pot(pot)
loss_valid.calc()
valid_errors = loss_valid.calc_errors()

if rank == 0:
    n_params = int(len(pot.params))

    with open(MODEL_PATH, "wb") as f:
        f.write(pot.to_json_bytes())

    metrics = {
        "model_label": "MTP-20",
        "model_type": "mtp",
        "dataset": "water_H2O",
        "species_order": species_order,
        "level": 20,
        "n_params": n_params,

        "train_db": TRAIN_DB,
        "valid_db": VALID_DB,
        "out_dir": OUT_DIR,
        "model_path": MODEL_PATH,

        "sbatch_file": f"{OUT_DIR}/train_water_mtp20_clean.sbatch",
        "exact_command_file": f"{OUT_DIR}/exact_command.txt",

        "created_at": datetime.now().isoformat(timespec="seconds"),
        "hostname": socket.gethostname(),
        "slurm_job_id": os.environ.get("SLURM_JOB_ID"),
        "slurm_nodelist": os.environ.get("SLURM_NODELIST"),
        "slurm_ntasks": os.environ.get("SLURM_NTASKS"),

        "train_result": str(train_result),
        "raw_errors": {
            "train": str(train_errors),
            "valid": str(valid_errors),
        },
        "metrics": {
            "train": numeric_metrics_from_errors(train_errors),
            "valid": numeric_metrics_from_errors(valid_errors),
        },
    }

    with open(METRICS_JSON_PATH, "w") as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False)

    write_metrics_csv(METRICS_CSV_PATH, metrics)

    print(train_result)
    print("TRAIN:", train_errors)
    print("VALID:", valid_errors)
    print("Saved model to:", MODEL_PATH)
    print("Saved metrics JSON to:", METRICS_JSON_PATH)
    print("Saved metrics CSV to:", METRICS_CSV_PATH)
