#!/usr/bin/env python
# coding: utf-8
"""
Train MTP level 20 on MoNbTaVW alloy dataset.
Data is already in mlip-4 LossFunction JSON format.
Stress weights are already zero — no fix needed.
"""

import os
import json
import numpy as np
from mpi4py import MPI
from mlip_4 import LossFunction, RadialBasisCinf, MTP, Trainer

# V(23), Nb(41), Mo(42), Ta(73), W(74) — sorted by atomic number
species_order = [23, 41, 42, 73, 74]

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

BASE = "~/coursework/new_datasets"
TRAIN_DB = f"{BASE}/alloy/convert/train_alloy.json"
VALID_DB = f"{BASE}/alloy/convert/valid_alloy.json"

OUT_DIR = f"{BASE}/alloy/mtp"
MODEL_PATH = f"{OUT_DIR}/mtp20_trained.json"
METRICS_PATH = f"{OUT_DIR}/metrics_20.json"

if rank == 0:
    os.makedirs(OUT_DIR, exist_ok=True)

# ---------- load train ----------
train_bytes = b""
if rank == 0:
    with open(TRAIN_DB, "rb") as f:
        train_bytes = f.read()
train_bytes = comm.bcast(train_bytes, root=0)
loss_train = LossFunction.from_json_bytes(train_bytes, True)

# ---------- load valid ----------
valid_bytes = b""
if rank == 0:
    with open(VALID_DB, "rb") as f:
        valid_bytes = f.read()
valid_bytes = comm.bcast(valid_bytes, root=0)
loss_valid = LossFunction.from_json_bytes(valid_bytes, True)

# ---------- create potential ----------
pot_bytes = b""
if rank == 0:
    np.random.seed(42)
    rb = RadialBasisCinf(size=8, min_dist=1.0, cutoff=5.0)
    pot = MTP(rb, species_order, level=20, jit=True)
    pot.params[:] = np.random.uniform(low=-1e-3, high=1e-3, size=len(pot.params))
    pot_bytes = pot.to_json_bytes()
    print(f"MTP level 20: {len(pot.params)} parameters, {len(species_order)} species")

pot_bytes = comm.bcast(pot_bytes, root=0)
pot = MTP.from_json_bytes(pot_bytes)

# ---------- train ----------
trainer = Trainer(loss_train)
train_result = trainer.train(pot, max_iter_count=2000)

# ---------- errors: train ----------
loss_train.attach_pot(pot)
loss_train.calc()
train_errors = loss_train.calc_errors()

# ---------- errors: valid ----------
loss_valid.attach_pot(pot)
loss_valid.calc()
valid_errors = loss_valid.calc_errors()

if rank == 0:
    with open(MODEL_PATH, "wb") as f:
        f.write(pot.to_json_bytes())

    metrics = {
        "dataset": "alloy_MoNbTaVW",
        "species_order": species_order,
        "level": 20,
        "train_db": TRAIN_DB,
        "valid_db": VALID_DB,
        "model_path": MODEL_PATH,
        "train_result": str(train_result),
        "train_errors": str(train_errors),
        "valid_errors": str(valid_errors),
    }

    with open(METRICS_PATH, "w") as f:
        json.dump(metrics, f, indent=2)

    print(train_result)
    print("TRAIN:", train_errors)
    print("VALID:", valid_errors)
    print("Saved model to:", MODEL_PATH)
    print("Saved metrics to:", METRICS_PATH)
