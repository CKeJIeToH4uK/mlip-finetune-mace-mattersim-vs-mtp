#!/bin/bash
set -euo pipefail

LR_LIST=(1e-4 5e-5 2e-5 1e-5)
BS_LIST=(8 16 32 64)

for lr in "${LR_LIST[@]}"; do
  for bs in "${BS_LIST[@]}"; do
    if [[ "$bs" == "8" && "$lr" == "1e-4" ]]; then
      echo "skip lr=$lr bs=$bs"
      continue
    fi
    echo "submit lr=$lr bs=$bs"
    sbatch --export=ALL,LR=$lr,BS=$bs ms_sweep.sh
  done
done