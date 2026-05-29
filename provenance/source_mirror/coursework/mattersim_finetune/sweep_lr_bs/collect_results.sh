import os
import re
import csv

base = "~/coursework/mattersim_finetune/sweep_lr_bs/runs"
rows = []

for run in os.listdir(base):
    path = os.path.join(base, run, "train.log")
    if not os.path.exists(path):
        continue

    lr = float(re.search(r"lr([^_]+)", run).group(1))
    bs = int(re.search(r"bs(\d+)", run).group(1))

    best_val = float("inf")

    with open(path) as f:
        for line in f:
            if "val:" in line and "MAE(f)" in line:
                val = float(re.search(r"MAE\(f\): ([0-9.]+)", line).group(1))
                best_val = min(best_val, val)

    rows.append([lr, bs, best_val])

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["lr", "batch_size", "best_val_MAE_f"])
    writer.writerows(rows)

print("Saved results.csv")