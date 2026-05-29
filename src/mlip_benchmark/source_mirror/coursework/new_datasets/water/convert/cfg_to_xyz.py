#!/usr/bin/env python3
# coding: utf-8
"""
Convert MLIP .cfg file to extxyz format.
Parses BEGIN_CFG...END_CFG blocks, maps integer types to atomic numbers,
writes ASE-compatible extended xyz with energy and forces.
"""

import argparse
import re
import numpy as np
from ase import Atoms
from ase.calculators.singlepoint import SinglePointCalculator
from ase.io import write


def parse_type2z(s):
    out = {}
    for item in s.split(","):
        k, v = item.split(":")
        out[int(k)] = int(v)
    return out


def iter_blocks(text):
    blocks, cur = [], None
    for line in text.splitlines():
        if "BEGIN_CFG" in line:
            cur = [line]
        elif cur is not None:
            cur.append(line)
            if "END_CFG" in line:
                blocks.append(cur)
                cur = None
    return blocks


def parse_block(lines, type2z):
    nat = None
    cell = None
    types, pos, forces = None, None, None
    energy = None

    i = 0
    while i < len(lines):
        s = lines[i].strip()

        if s.lower() == "size":
            i += 1
            nat = int(lines[i].split()[0])

        elif s.lower() == "supercell":
            a = []
            for _ in range(3):
                i += 1
                a.append([float(x) for x in lines[i].split()[:3]])
            cell = np.array(a)

        elif s.startswith("AtomData:"):
            cols = s.split(":", 1)[1].split()
            itype = cols.index("type") if "type" in cols else None
            ix = cols.index("cartes_x") if "cartes_x" in cols else None
            iy = cols.index("cartes_y") if "cartes_y" in cols else None
            iz = cols.index("cartes_z") if "cartes_z" in cols else None

            # id is first column, but numbering in cols starts from 'id'
            # columns: id type cartes_x cartes_y cartes_z fx fy fz
            ifx = cols.index("fx") if "fx" in cols else None
            ify = cols.index("fy") if "fy" in cols else None
            ifz = cols.index("fz") if "fz" in cols else None

            types = np.zeros(nat, dtype=int)
            pos = np.zeros((nat, 3))
            has_forces = ifx is not None and ify is not None and ifz is not None
            if has_forces:
                forces = np.zeros((nat, 3))

            for a in range(nat):
                i += 1
                p = lines[i].split()
                types[a] = int(p[itype])
                pos[a] = [float(p[ix]), float(p[iy]), float(p[iz])]
                if has_forces:
                    forces[a] = [float(p[ifx]), float(p[ify]), float(p[ifz])]

        elif s.startswith("Energy"):
            nums = re.findall(r"[-+]?\d+\.?\d*(?:[eE][-+]?\d+)?", s)
            if nums:
                energy = float(nums[-1])
            else:
                i += 1
                nums = re.findall(r"[-+]?\d+\.?\d*(?:[eE][-+]?\d+)?", lines[i])
                if nums:
                    energy = float(nums[-1])

        i += 1

    numbers = [type2z[t] for t in types]
    atoms = Atoms(numbers=numbers, positions=pos, cell=cell, pbc=True)

    sp_kwargs = {}
    if energy is not None:
        sp_kwargs["energy"] = energy
    if forces is not None:
        sp_kwargs["forces"] = forces
    if sp_kwargs:
        atoms.calc = SinglePointCalculator(atoms, **sp_kwargs)

    return atoms


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_cfg")
    parser.add_argument("output_xyz")
    parser.add_argument("--type2z", required=True,
                        help="Mapping like 0:1,1:8 (type:atomic_number)")
    args = parser.parse_args()

    type2z = parse_type2z(args.type2z)

    with open(args.input_cfg, "r", errors="replace") as f:
        text = f.read()

    blocks = iter_blocks(text)
    print(f"Found {len(blocks)} configs in {args.input_cfg}")

    atoms_list = [parse_block(b, type2z) for b in blocks]

    write(args.output_xyz, atoms_list, format="extxyz")
    print(f"Saved {len(atoms_list)} configs to {args.output_xyz}")


if __name__ == "__main__":
    main()
