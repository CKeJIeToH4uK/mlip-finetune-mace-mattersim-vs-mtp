#!/usr/bin/env python
# coding: utf-8

import argparse
import json
import os
import re
from mpi4py import MPI
from mlip_4 import LossFunction, MTP

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def parse_errors(err_text: str):
    def extract(line_name):
        pattern = rf"{re.escape(line_name)}\s*=\s*([0-9eE+\-.]+),\s*([0-9eE+\-.]+),\s*([0-9eE+\-.]+)"
        m = re.search(pattern, err_text)
        if not m:
            return None
        return {
            "mae": float(m.group(1)),
            "rmse": float(m.group(2)),
            "maxae": float(m.group(3)),
        }

    return {
        "energy": extract("Energy"),
        "energy_per_atom": extract("Energy/Atom"),
        "forces": extract("Forces"),
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", required=True)
    parser.add_argument("--test_path", required=True)
    parser.add_argument("--output_json", required=True)
    parser.add_argument("--dataset_name", default=None)
    parser.add_argument("--model_name", default="mtp")
    args = parser.parse_args()

    test_bytes = b""
    if rank == 0:
        with open(args.test_path, "rb") as f:
            test_bytes = f.read()
    test_bytes = comm.bcast(test_bytes, root=0)
    loss_test = LossFunction.from_json_bytes(test_bytes, True)

    pot_bytes = b""
    if rank == 0:
        with open(args.model_path, "rb") as f:
            pot_bytes = f.read()
    pot_bytes = comm.bcast(pot_bytes, root=0)
    pot = MTP.from_json_bytes(pot_bytes)

    loss_test.attach_pot(pot)
    loss_test.calc()
    test_errors = loss_test.calc_errors()
    raw = str(test_errors)
    parsed = parse_errors(raw)

    result = {
        "model_type": "mtp",
        "model_name": args.model_name,
        "model_path": args.model_path,
        "dataset_path": args.test_path,
        "dataset_name": args.dataset_name,
        "raw_errors": raw,
        "mae_E_eV": parsed["energy"]["mae"] if parsed["energy"] else None,
        "rmse_E_eV": parsed["energy"]["rmse"] if parsed["energy"] else None,
        "mae_E_per_atom_eV": parsed["energy_per_atom"]["mae"] if parsed["energy_per_atom"] else None,
        "rmse_E_per_atom_eV": parsed["energy_per_atom"]["rmse"] if parsed["energy_per_atom"] else None,
        "mae_F_eV_A": parsed["forces"]["mae"] if parsed["forces"] else None,
        "rmse_F_eV_A": parsed["forces"]["rmse"] if parsed["forces"] else None,
        "mae_F_meV_A": 1000.0 * parsed["forces"]["mae"] if parsed["forces"] else None,
        "rmse_F_meV_A": 1000.0 * parsed["forces"]["rmse"] if parsed["forces"] else None,
    }

    if rank == 0:
        os.makedirs(os.path.dirname(args.output_json), exist_ok=True)
        with open(args.output_json, "w") as f:
            json.dump(result, f, indent=2)
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()