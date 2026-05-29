#!/usr/bin/env python
# coding: utf-8

import csv
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
RUNS = ["full_ew10_normal", "full_ew50_normal"]

rows = []

for run in RUNS:
    for split in ["train", "valid"]:
        p = BASE / run / f"eval_{split}.json"
        if not p.exists():
            continue

        with open(p, encoding="utf-8") as f:
            d = json.load(f)

        rows.append({
            "run": run,
            "split": split,
            "metric": "energy",
            "mae": d["mae_E_per_atom_meV"],
            "rmse": d["rmse_E_per_atom_meV"],
            "units": "meV/atom",
            "model_path": d["model_path"],
        })
        rows.append({
            "run": run,
            "split": split,
            "metric": "forces",
            "mae": d["mae_F_meV_A"],
            "rmse": d["rmse_F_meV_A"],
            "units": "meV/Å",
            "model_path": d["model_path"],
        })

csv_path = BASE / "ew10_ew50_normal_metrics_long.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["run", "split", "metric", "mae", "rmse", "units", "model_path"],
    )
    writer.writeheader()
    writer.writerows(rows)


def get(run, split, metric, field):
    for r in rows:
        if r["run"] == run and r["split"] == split and r["metric"] == metric:
            return r[field]
    return None


md = []
md.append("# EW10 / EW50 normal MACE alloy metrics")
md.append("")
md.append("Baseline fair200 valid:")
md.append("")
md.append("| run | E MAE | E RMSE | F MAE | F RMSE |")
md.append("|---|---:|---:|---:|---:|")
md.append("| fair200 baseline | 27.523 | 86.401 | 62.076 | 113.747 |")
md.append("")
md.append("Normal runs valid:")
md.append("")
md.append("| run | E MAE, meV/atom | E RMSE, meV/atom | F MAE, meV/Å | F RMSE, meV/Å |")
md.append("|---|---:|---:|---:|---:|")

for run in RUNS:
    md.append(
        f"| {run} | "
        f"{get(run, 'valid', 'energy', 'mae')} | "
        f"{get(run, 'valid', 'energy', 'rmse')} | "
        f"{get(run, 'valid', 'forces', 'mae')} | "
        f"{get(run, 'valid', 'forces', 'rmse')} |"
    )

md.append("")
md.append("Normal runs train:")
md.append("")
md.append("| run | E MAE, meV/atom | E RMSE, meV/atom | F MAE, meV/Å | F RMSE, meV/Å |")
md.append("|---|---:|---:|---:|---:|")

for run in RUNS:
    md.append(
        f"| {run} | "
        f"{get(run, 'train', 'energy', 'mae')} | "
        f"{get(run, 'train', 'energy', 'rmse')} | "
        f"{get(run, 'train', 'forces', 'mae')} | "
        f"{get(run, 'train', 'forces', 'rmse')} |"
    )

md_path = BASE / "ew10_ew50_normal_summary.md"
md_path.write_text("\n".join(md), encoding="utf-8")

print("Wrote:", csv_path)
print("Wrote:", md_path)
print(md_path.read_text(encoding="utf-8"))
