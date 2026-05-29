#!/usr/bin/env python
# coding: utf-8

import csv
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
RUNS = ["stage2_normal", "lora_ew10_normal", "freeze1_ew10_normal"]

rows = []

for run in RUNS:
    for split in ["train", "valid"]:
        path = BASE / run / f"eval_{split}.json"
        if not path.exists():
            continue

        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        rows.append({
            "run": run,
            "split": split,
            "metric": "energy",
            "mae": data["mae_E_per_atom_meV"],
            "rmse": data["rmse_E_per_atom_meV"],
            "units": "meV/atom",
            "model_path": data["model_path"],
        })
        rows.append({
            "run": run,
            "split": split,
            "metric": "forces",
            "mae": data["mae_F_meV_A"],
            "rmse": data["rmse_F_meV_A"],
            "units": "meV/Å",
            "model_path": data["model_path"],
        })

csv_path = BASE / "protocols_normal_metrics_long.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["run", "split", "metric", "mae", "rmse", "units", "model_path"],
    )
    writer.writeheader()
    writer.writerows(rows)


def get(run, split, metric, field):
    for row in rows:
        if row["run"] == run and row["split"] == split and row["metric"] == metric:
            return row[field]
    return None


def add_table(md, title, split):
    md.append(title)
    md.append("")
    md.append("| run | E MAE | E RMSE | F MAE | F RMSE |")
    md.append("|---|---:|---:|---:|---:|")
    for run in RUNS:
        md.append(
            f"| {run} | "
            f"{get(run, split, 'energy', 'mae')} | "
            f"{get(run, split, 'energy', 'rmse')} | "
            f"{get(run, split, 'forces', 'mae')} | "
            f"{get(run, split, 'forces', 'rmse')} |"
        )
    md.append("")


md = []
md.append("# Protocols Normal MACE Alloy Metrics")
md.append("")
md.append("Baseline fair200 valid:")
md.append("")
md.append("| reference | E MAE | E RMSE | F MAE | F RMSE |")
md.append("|---|---:|---:|---:|---:|")
md.append("| fair200 | 27.523 | 86.401 | 62.076 | 113.747 |")
md.append("")
md.append("EW10 partial quick reference:")
md.append("")
md.append("| reference | E RMSE | F RMSE |")
md.append("|---|---:|---:|")
md.append("| Epoch 125 | ~29.00 | ~115.09 |")
md.append("")
add_table(md, "Valid metrics:", "valid")
add_table(md, "Train metrics:", "train")
md.append("Interpretation:")
md.append("- A useful run lowers energy RMSE substantially without making force RMSE much worse.")
md.append("- If stage2/LoRA/freeze do not beat EW10/EW50, keep them as negative/backup ablations.")
md.append("- Main result remains energy-weighted MACE if protocol variants do not improve.")

md_path = BASE / "protocols_normal_summary.md"
md_path.write_text("\n".join(md) + "\n", encoding="utf-8")

print("Wrote:", csv_path)
print("Wrote:", md_path)
print(md_path.read_text(encoding="utf-8"))
