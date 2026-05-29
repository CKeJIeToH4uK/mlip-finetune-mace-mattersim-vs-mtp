#!/usr/bin/env python
# coding: utf-8
"""
Convert extxyz to mlip-4 LossFunction JSON format.
Copied from coursework/cross_temp_eval/scripts/xyz_to_mtp_json.py
"""

import argparse
import json
import numpy as np
from ase import Atoms
from ase.calculators.singlepoint import SinglePointCalculator
from ase.io import read
from mlip_4 import CalcCfg


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_xyz", required=True)
    parser.add_argument("--output_json", required=True)
    args = parser.parse_args()

    atoms_list = read(args.input_xyz, ":")

    data = []
    for a in atoms_list:
        e = float(a.get_potential_energy())
        f = np.array(a.get_forces(), dtype=np.float64, order="C", copy=True)

        pos = np.array(a.positions, dtype=np.float64, order="C", copy=True)
        cell = np.array(a.cell.array, dtype=np.float64, order="C", copy=True)

        a2 = Atoms(numbers=a.numbers, positions=pos, cell=cell, pbc=a.pbc)
        a2.calc = SinglePointCalculator(a2, energy=e, forces=f)

        cfg = CalcCfg.from_ase(a2)
        sim = json.loads(cfg.to_json_bytes().decode("utf-8"))

        nat = len(a2)
        weights = [1.0] + [0.0]*9 + [0.01]*(3*nat)
        data.append({"sim": sim, "weights": weights})

    with open(args.output_json, "w", encoding="utf-8") as out:
        json.dump(data, out, ensure_ascii=False)

    print("OK:", len(data))
    print("Saved to:", args.output_json)


if __name__ == "__main__":
    main()
