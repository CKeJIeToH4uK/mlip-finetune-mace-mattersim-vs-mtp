#!/usr/bin/env python3
"""
Конвертер mlip-4 train.json -> ASE extxyz + split.

Мапа типов для FLiNaK (порядок от И. Новикова): 0=F, 1=K, 2=Li, 3=Na.

Использование:
    python json_to_xyz_split.py \
        --input data/train.json \
        --out-all data/train_all.xyz \
        --out-train data/train_90.xyz \
        --out-valid data/valid_10.xyz \
        --valid-fraction 0.10 \
        --seed 42
"""
import argparse
import json
import random
from pathlib import Path

TYPE_TO_SYMBOL = {0: "F", 1: "K", 2: "Li", 3: "Na"}


def cfg_to_extxyz(entry: dict) -> str:
    sim = entry["sim"]
    cfg = sim["cfg"]
    cell = cfg["cell"]
    pos = cfg["pos"]
    types = cfg["types"]
    forces = sim["forces"]
    energy = sim["energy"]

    n = len(pos)
    assert len(types) == n == len(forces), f"mismatch n={n} types={len(types)} forces={len(forces)}"

    lattice = " ".join(
        f"{v:.8f}" for row in cell for v in row
    )
    header = (
        f'Lattice="{lattice}" '
        f'Properties=species:S:1:pos:R:3:forces:R:3 '
        f'energy={energy:.8f} pbc="T T T"'
    )

    lines = [str(n), header]
    for t, (x, y, z), (fx, fy, fz) in zip(types, pos, forces):
        sym = TYPE_TO_SYMBOL[t]
        lines.append(
            f"{sym} {x:.8f} {y:.8f} {z:.8f} {fx:.8f} {fy:.8f} {fz:.8f}"
        )
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, type=Path)
    ap.add_argument("--out-all", required=True, type=Path)
    ap.add_argument("--out-train", required=True, type=Path)
    ap.add_argument("--out-valid", required=True, type=Path)
    ap.add_argument("--valid-fraction", type=float, default=0.10)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    with args.input.open() as f:
        data = json.load(f)

    n_total = len(data)
    print(f"loaded {n_total} configs from {args.input}")

    xyz_blocks = [cfg_to_extxyz(e) for e in data]

    args.out_all.parent.mkdir(parents=True, exist_ok=True)
    with args.out_all.open("w") as f:
        f.writelines(xyz_blocks)
    print(f"wrote ALL -> {args.out_all} ({n_total} cfgs)")

    rng = random.Random(args.seed)
    idx = list(range(n_total))
    rng.shuffle(idx)
    n_valid = max(1, int(round(n_total * args.valid_fraction)))
    valid_idx = set(idx[:n_valid])

    train_blocks = [b for i, b in enumerate(xyz_blocks) if i not in valid_idx]
    valid_blocks = [b for i, b in enumerate(xyz_blocks) if i in valid_idx]

    with args.out_train.open("w") as f:
        f.writelines(train_blocks)
    print(f"wrote TRAIN -> {args.out_train} ({len(train_blocks)} cfgs)")

    with args.out_valid.open("w") as f:
        f.writelines(valid_blocks)
    print(f"wrote VALID -> {args.out_valid} ({len(valid_blocks)} cfgs)")


if __name__ == "__main__":
    main()
