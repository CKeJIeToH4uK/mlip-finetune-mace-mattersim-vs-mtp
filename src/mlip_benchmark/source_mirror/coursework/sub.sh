#!/bin/bash
sbatch -p normal -A proj_1786 -N 1 -n 4 -J mtp_train \
  --output=logs_20_1/%x_%j.out \
  ./run.sh