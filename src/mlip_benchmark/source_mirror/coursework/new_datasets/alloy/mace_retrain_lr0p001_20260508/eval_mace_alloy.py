#!/usr/bin/env python
# coding: utf-8

import argparse
import json
import os
import time

import numpy as np
import torch
from ase.io import read
from mace.calculators import MACECalculator


def eval_mace(model_path, test_path, output_json, dataset_name=None):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    cfgs = read(test_path, ":")

    calc = MACECalculator(model_paths=model_path, device=device)

    # warmup
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
        "model_type": "mace",
        "model_path": model_path,
        "dataset_path": test_path,
        "dataset_name": dataset_name,
        "n_cfg": int(len(cfgs)),

        "rmse_E_per_atom_eV": rmse_E_eV,
        "mae_E_per_atom_eV": mae_E_eV,
        "rmse_E_per_atom_meV": 1000.0 * rmse_E_eV,
        "mae_E_per_atom_meV": 1000.0 * mae_E_eV,

        "rmse_F_eV_A": rmse_F_eV,
        "mae_F_eV_A": mae_F_eV,
        "rmse_F_meV_A": 1000.0 * rmse_F_eV,
        "mae_F_meV_A": 1000.0 * mae_F_eV,

        "time_sec_total": float(t1 - t0),
    }

    os.makedirs(os.path.dirname(output_json), exist_ok=True)

    with open(output_json, "w") as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", required=True)
    parser.add_argument("--test_path", required=True)
    parser.add_argument("--output_json", required=True)
    parser.add_argument("--dataset_name", default=None)
    args = parser.parse_args()

    eval_mace(
        model_path=args.model_path,
        test_path=args.test_path,
        output_json=args.output_json,
        dataset_name=args.dataset_name,
    )
