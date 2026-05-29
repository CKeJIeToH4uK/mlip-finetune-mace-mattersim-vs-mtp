#!/usr/bin/env python
# coding: utf-8

import argparse
import csv
import json
import os
import time

import numpy as np
import torch
from ase.io import read
from mace.calculators import MACECalculator


def eval_mace(model_path, test_path, output_json, dataset_name=None, split=None):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    cfgs = read(test_path, ":")

    calc = MACECalculator(model_paths=model_path, device=device)

    if len(cfgs) > 0:
        atoms = cfgs[0]
        old_calc = atoms.calc
        atoms.calc = calc
        _ = atoms.get_potential_energy()
        _ = atoms.get_forces()
        atoms.calc = old_calc

        if device == "cuda":
            torch.cuda.synchronize()

    t0 = time.perf_counter()

    e_ref_list = []
    e_pred_list = []
    n_atoms_list = []

    sq_f = 0.0
    abs_f = 0.0
    cnt_f = 0

    for atoms in cfgs:
        e_ref = atoms.get_potential_energy()
        f_ref = atoms.get_forces()

        old_calc = atoms.calc
        atoms.calc = calc
        e_pred = atoms.get_potential_energy()
        f_pred = atoms.get_forces()
        atoms.calc = old_calc

        e_ref_list.append(e_ref)
        e_pred_list.append(e_pred)
        n_atoms_list.append(len(atoms))

        df = (f_pred - f_ref).reshape(-1)
        sq_f += float(np.dot(df, df))
        abs_f += float(np.sum(np.abs(df)))
        cnt_f += df.size

    if device == "cuda":
        torch.cuda.synchronize()

    t1 = time.perf_counter()

    e_ref_arr = np.array(e_ref_list)
    e_pred_arr = np.array(e_pred_list)
    n_atoms_arr = np.array(n_atoms_list, dtype=float)

    dE_per_atom = (e_pred_arr - e_ref_arr) / n_atoms_arr

    rmse_E_eV = float(np.sqrt(np.mean(dE_per_atom ** 2)))
    mae_E_eV = float(np.mean(np.abs(dE_per_atom)))

    rmse_F_eV = float(np.sqrt(sq_f / cnt_f))
    mae_F_eV = float(abs_f / cnt_f)

    result = {
        "model_label": "MACE",
        "model_type": "mace",
        "run_type": "fair200_quick3h_lr0p001",
        "model_path": model_path,
        "dataset_path": test_path,
        "dataset_name": dataset_name,
        "split": split,
        "n_cfg": int(len(cfgs)),

        "rmse_E_per_atom_eV": rmse_E_eV,
        "mae_E_per_atom_eV": mae_E_eV,
        "rmse_E_per_atom_meV": 1000.0 * rmse_E_eV,
        "mae_E_per_atom_meV": 1000.0 * mae_E_eV,

        "rmse_F_eV_A": rmse_F_eV,
        "mae_F_eV_A": mae_F_eV,
        "rmse_F_meV_A": 1000.0 * rmse_F_eV,
        "mae_F_meV_A": 1000.0 * mae_F_eV,

        "energy_units": "meV/atom",
        "forces_units": "meV/Å",
        "time_sec_total": float(t1 - t0),
    }

    os.makedirs(os.path.dirname(output_json), exist_ok=True)

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return result


def write_summary_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
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
                "run_type",
                "model_path",
            ],
        )
        writer.writeheader()

        for row in rows:
            writer.writerow({
                "model_label": "MACE",
                "dataset": "alloy_MoNbTaVW",
                "split": row["split"],
                "metric": "energy",
                "mae": row["mae_E_per_atom_meV"],
                "rmse": row["rmse_E_per_atom_meV"],
                "units": "meV/atom",
                "run_type": row["run_type"],
                "model_path": row["model_path"],
            })
            writer.writerow({
                "model_label": "MACE",
                "dataset": "alloy_MoNbTaVW",
                "split": row["split"],
                "metric": "forces",
                "mae": row["mae_F_meV_A"],
                "rmse": row["rmse_F_meV_A"],
                "units": "meV/Å",
                "run_type": row["run_type"],
                "model_path": row["model_path"],
            })


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", required=True)
    parser.add_argument("--train_path", required=True)
    parser.add_argument("--valid_path", required=True)
    parser.add_argument("--out_dir", required=True)
    args = parser.parse_args()

    valid = eval_mace(
        model_path=args.model_path,
        test_path=args.valid_path,
        output_json=os.path.join(args.out_dir, "eval_valid.json"),
        dataset_name="alloy_valid_lr0p001_fair200_quick3h",
        split="valid",
    )

    train = eval_mace(
        model_path=args.model_path,
        test_path=args.train_path,
        output_json=os.path.join(args.out_dir, "eval_train.json"),
        dataset_name="alloy_train_lr0p001_fair200_quick3h",
        split="train",
    )

    write_summary_csv(
        os.path.join(args.out_dir, "eval_metrics_fair200_quick3h.csv"),
        [train, valid],
    )
