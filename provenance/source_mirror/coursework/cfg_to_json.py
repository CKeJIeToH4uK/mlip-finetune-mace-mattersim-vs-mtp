#!/usr/bin/env python3
# coding: utf-8

import argparse
import json
import re
from typing import Dict, List, Optional, Tuple

import numpy as np
from ase import Atoms
from ase.calculators.singlepoint import SinglePointCalculator

from mlip_4 import CalcCfg


FLOAT_RE = re.compile(r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?")


def _next_nonempty(lines: List[str], i: int) -> Tuple[int, str]:
    j = i + 1
    while j < len(lines) and not lines[j].strip():
        j += 1
    if j >= len(lines):
        raise ValueError("Unexpected EOF while parsing cfg block")
    return j, lines[j].strip()


def iter_blocks(text: str) -> List[List[str]]:
    blocks = []
    cur = None
    for line in text.splitlines():
        if "BEGIN_CFG" in line:
            cur = [line]
        elif cur is not None:
            cur.append(line)
            if "END_CFG" in line:
                blocks.append(cur)
                cur = None
    return blocks


def parse_energy(line: str, lines: List[str], i: int) -> Tuple[Optional[float], int]:
    # Energy may be on the same line or on the next line
    nums = FLOAT_RE.findall(line)
    if nums:
        return float(nums[-1]), i
    j, nxt = _next_nonempty(lines, i)
    nums = FLOAT_RE.findall(nxt)
    if not nums:
        return None, j
    return float(nums[-1]), j


def col_idx(cols: List[str], names: List[str]) -> Optional[int]:
    for n in names:
        if n in cols:
            return cols.index(n)
    return None


def parse_block(block: List[str], type2z: Dict[int, int], default_z: int) -> dict:
    lines = [l.rstrip() for l in block]
    nat = None
    cell = None
    types = None
    pos = None
    forces = None
    energy = None

    i = 0
    while i < len(lines):
        s = lines[i].strip()

        if s.lower() == "size":
            j, nxt = _next_nonempty(lines, i)
            nat = int(nxt.split()[0])
            i = j

        elif s.lower() == "supercell":
            a = []
            for k in range(3):
                j, nxt = _next_nonempty(lines, i + k)
                a.append([float(x) for x in nxt.split()[:3]])
            cell = np.array(a, dtype=float)
            i = i + 3

        elif s.startswith("AtomData:"):
            if nat is None:
                raise ValueError("Size must appear before AtomData")

            cols = s.split(":", 1)[1].split()

            itype = col_idx(cols, ["type", "atom_type", "species", "z"])
            ix = col_idx(cols, ["cartes_x", "x", "pos_x"])
            iy = col_idx(cols, ["cartes_y", "y", "pos_y"])
            iz = col_idx(cols, ["cartes_z", "z", "pos_z"])
            if ix is None or iy is None or iz is None or itype is None:
                raise ValueError(f"Unsupported AtomData columns: {cols}")

            ifx = col_idx(cols, ["fx", "force_x", "f_x"])
            ify = col_idx(cols, ["fy", "force_y", "f_y"])
            ifz = col_idx(cols, ["fz", "force_z", "f_z"])

            types = np.zeros(nat, dtype=int)
            pos = np.zeros((nat, 3), dtype=float)
            has_forces = (ifx is not None) and (ify is not None) and (ifz is not None)
            if has_forces:
                forces = np.zeros((nat, 3), dtype=float)

            for a in range(nat):
                i += 1
                parts = lines[i].split()
                types[a] = int(float(parts[itype]))
                pos[a, :] = [float(parts[ix]), float(parts[iy]), float(parts[iz])]
                if has_forces:
                    forces[a, :] = [float(parts[ifx]), float(parts[ify]), float(parts[ifz])]

        elif s.startswith("Energy"):
            energy, i = parse_energy(s, lines, i)

        i += 1

    if nat is None or cell is None or types is None or pos is None:
        raise ValueError("Incomplete cfg block (need Size, SuperCell, AtomData)")

    # map MLIP "type" -> atomic numbers
    numbers = []
    for t in types.tolist():
        numbers.append(type2z.get(int(t), default_z))
    numbers = np.array(numbers, dtype=int)

    atoms = Atoms(numbers=numbers, positions=pos, cell=cell, pbc=True)

    # attach energy/forces (if present) via SinglePointCalculator
    sp_kwargs = {}
    if energy is not None:
        sp_kwargs["energy"] = float(energy)
    if forces is not None:
        sp_kwargs["forces"] = np.asarray(forces, dtype=float)
    if sp_kwargs:
        atoms.calc = SinglePointCalculator(atoms, **sp_kwargs)

    cfg = CalcCfg.from_ase(atoms)

    # export ONE config as python dict
    if hasattr(cfg, "to_json_bytes"):
        return json.loads(cfg.to_json_bytes().decode("utf-8"))
    if hasattr(cfg, "to_json"):
        j = cfg.to_json()
        if isinstance(j, (dict, list)):
            return j
        if isinstance(j, (bytes, bytearray)):
            return json.loads(j.decode("utf-8"))
        if isinstance(j, str):
            return json.loads(j)
    raise RuntimeError("CalcCfg can't be serialized (no to_json/to_json_bytes)")


def parse_type2z(s: str) -> Dict[int, int]:
    # "0:13,1:42" -> {0:13, 1:42}
    out = {}
    if not s:
        return out
    for item in s.split(","):
        k, v = item.split(":")
        out[int(k)] = int(v)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input_cfg")
    ap.add_argument("output_json")
    ap.add_argument("--default-z", type=int, default=13, help="Atomic number for unmapped types (default: 13 for Al)")
    ap.add_argument("--type2z", type=str, default="", help="Mapping like 0:13,1:42")
    ap.add_argument("--we", type=float, default=1.0, help="Energy weight (default: 1.0)")
    ap.add_argument("--wf", type=float, default=0.01, help="Forces weight per component (default: 0.01)")
    ap.add_argument("--ws", type=float, default=0.0, help="Stress weight (default: 0.0)")
    args = ap.parse_args()

    type2z = parse_type2z(args.type2z)

    with open(args.input_cfg, "r", encoding="utf-8", errors="replace") as f:
        text = f.read()

    blocks = iter_blocks(text)
    if not blocks:
        raise SystemExit("No BEGIN_CFG ... END_CFG blocks found")

    # Parse configs (CalcCfg JSON)
    sims = [parse_block(b, type2z=type2z, default_z=args.default_z) for b in blocks]

    # Wrap into LossFunction-like JSON: {"sim": ..., "weights": ...}
    data = []
    for sim in sims:
        # nat from positions length
        nat = len(sim["cfg"]["pos"])
        weights = [float(args.we)] + [float(args.ws)] * 9 + [float(args.wf)] * (3 * nat)
        data.append({"sim": sim, "weights": weights})

    with open(args.output_json, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"OK: {len(data)} configs -> {args.output_json}")


if __name__ == "__main__":
    main()
