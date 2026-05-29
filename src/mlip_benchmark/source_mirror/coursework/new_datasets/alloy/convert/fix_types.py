#!/usr/bin/env python3
# coding: utf-8
"""
Remap types in mlip-4 LossFunction JSON from indices (0-4) to atomic numbers.
MoNbTaVW: 0->V(23), 1->Nb(41), 2->Mo(42), 3->Ta(73), 4->W(74)
"""

import argparse
import json

TYPE_MAP = {0: 23, 1: 41, 2: 42, 3: 73, 4: 74}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json")
    parser.add_argument("output_json")
    args = parser.parse_args()

    with open(args.input_json, "r") as f:
        data = json.load(f)

    for d in data:
        old_types = d["sim"]["cfg"]["types"]
        d["sim"]["cfg"]["types"] = [TYPE_MAP[t] for t in old_types]

    with open(args.output_json, "w") as f:
        json.dump(data, f, ensure_ascii=False)

    print(f"Remapped {len(data)} configs: {list(TYPE_MAP.items())}")
    print(f"Saved to {args.output_json}")


if __name__ == "__main__":
    main()
