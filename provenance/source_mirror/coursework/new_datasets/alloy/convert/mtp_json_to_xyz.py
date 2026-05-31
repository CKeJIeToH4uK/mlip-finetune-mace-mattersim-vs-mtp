#!/usr/bin/env python3
# coding: utf-8
"""
Convert mlip-4 LossFunction JSON to extxyz format.
Used for MoNbTaVW alloy: types 0-4 -> V(23), Nb(41), Mo(42), Ta(73), W(74).
"""

import argparse
import json
import numpy as np
from ase import Atoms
from ase.calculators.singlepoint import SinglePointCalculator
from ase.io import write


# MoNbTaVW type mapping (sorted by atomic number)
TYPE2Z = {0: 23, 1: 41, 2: 42, 3: 73, 4: 74}
TYPE2SYM = {0: "V", 1: "Nb", 2: "Mo", 3: "Ta", 4: "W"}


def convert(input_json, output_xyz, type2z=None):
    if type2z is None:
        type2z = TYPE2Z

    with open(input_json, "r") as f:
        data = json.load(f)

    atoms_list = []
    for i, d in enumerate(data):
        sim = d["sim"]
        cfg = sim["cfg"]

        types = cfg["types"]
        positions = np.array(cfg["pos"], dtype=float)
        cell = np.array(cfg["cell"], dtype=float)
        numbers = [type2z[t] for t in types]

        atoms = Atoms(numbers=numbers, positions=positions, cell=cell, pbc=True)

        sp_kwargs = {}
        if "energy" in sim and sim["energy"] is not None:
            sp_kwargs["energy"] = float(sim["energy"])
        if "forces" in sim and sim["forces"] is not None:
            sp_kwargs["forces"] = np.array(sim["forces"], dtype=float)

        if sp_kwargs:
            atoms.calc = SinglePointCalculator(atoms, **sp_kwargs)

        atoms_list.append(atoms)

    write(output_xyz, atoms_list, format="extxyz")
    print(f"Converted {len(atoms_list)} configs from {input_json} -> {output_xyz}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json")
    parser.add_argument("output_xyz")
    parser.add_argument("--type2z", type=str, default="",
                        help="Override mapping, e.g. '0:23,1:41,2:42,3:73,4:74'")
    args = parser.parse_args()

    type2z = TYPE2Z
    if args.type2z:
        type2z = {}
        for item in args.type2z.split(","):
            k, v = item.split(":")
            type2z[int(k)] = int(v)

    convert(args.input_json, args.output_xyz, type2z)


if __name__ == "__main__":
    main()
