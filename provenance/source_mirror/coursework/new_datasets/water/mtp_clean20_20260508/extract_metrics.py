#!/usr/bin/env python
# coding: utf-8
"""
Lightweight metrics printer for clean H2O MTP-20 run.

Safe to run on login node after the SLURM job finished:
it only reads metrics_20_clean.json and prints numeric metrics.
"""

import argparse
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--metrics",
        default="metrics_20_clean.json",
        help="Path to metrics_20_clean.json",
    )
    args = parser.parse_args()

    with open(args.metrics) as f:
        d = json.load(f)

    print("model_label:", d["model_label"])
    print("dataset:", d["dataset"])
    print("level:", d["level"])
    print("n_params:", d["n_params"])
    print("model_path:", d["model_path"])
    print()

    for split in ["train", "valid"]:
        energy = d["metrics"][split]["energy"]
        forces = d["metrics"][split]["forces"]

        print(split.upper())
        print(f"  Energy MAE:  {energy['mae_meV_atom']:.6f} meV/atom")
        print(f"  Energy RMSE: {energy['rmse_meV_atom']:.6f} meV/atom")
        print(f"  Forces MAE:  {forces['mae_meV_A']:.6f} meV/Å")
        print(f"  Forces RMSE: {forces['rmse_meV_A']:.6f} meV/Å")
        print()


if __name__ == "__main__":
    main()
