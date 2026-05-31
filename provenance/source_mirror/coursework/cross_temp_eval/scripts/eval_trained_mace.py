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

    if len(cfgs) > 0:
        a0 = cfgs[0]
        old_calc = a0.calc
        a0.calc = calc
        _ = a0.get_potential_energy()
        _ = a0.get_forces()
        a0.calc = old_calc
        if device == "cuda":
            torch.cuda.synchronize()

    t0 = time.perf_counter()

    E_ref, E_pred, n_atoms = [], [], []
    sq_f, abs_f, cnt_f = 0.0, 0.0, 0

    for a in cfgs:
        e_ref = a.get_potential_energy()
        f_ref = a.get_forces()

        old_calc = a.calc
        a.calc = calc
        e_pred = a.get_potential_energy()
        f_pred = a.get_forces()
        a.calc = old_calc

        E_ref.append(e_ref)
        E_pred.append(e_pred)
        n_atoms.append(len(a))

        d = (f_pred - f_ref).reshape(-1)
        sq_f += float(np.dot(d, d))
        abs_f += float(np.sum(np.abs(d)))
        cnt_f += d.size

    if device == "cuda":
        torch.cuda.synchronize()
    t1 = time.perf_counter()

    E_ref = np.array(E_ref, dtype=float)
    E_pred = np.array(E_pred, dtype=float)
    n_atoms = np.array(n_atoms, dtype=float)

    dE_pa = (E_pred - E_ref) / n_atoms

    result = {
        "model_type": "mace",
        "model_path": model_path,
        "dataset_path": test_path,
        "dataset_name": dataset_name,
        "n_cfg": int(len(cfgs)),
        "rmse_E_per_atom_eV": float(np.sqrt(np.mean(dE_pa ** 2))),
        "mae_E_per_atom_eV": float(np.mean(np.abs(dE_pa))),
        "rmse_F_eV_A": float(np.sqrt(sq_f / cnt_f)),
        "mae_F_eV_A": float(abs_f / cnt_f),
        "rmse_F_meV_A": float(1000.0 * np.sqrt(sq_f / cnt_f)),
        "mae_F_meV_A": float(1000.0 * abs_f / cnt_f),
        "time_sec_total": float(t1 - t0),
    }

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

    os.makedirs(os.path.dirname(args.output_json), exist_ok=True)
    eval_mace(args.model_path, args.test_path, args.output_json, args.dataset_name)