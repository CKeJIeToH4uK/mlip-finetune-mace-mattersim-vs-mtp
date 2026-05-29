#!/bin/bash
#SBATCH -J mace_help_flags
#SBATCH -A proj_1786
#SBATCH -p test
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:10:00
#SBATCH -o mace_help_flags_%j.out

set -euo pipefail

export PYTHONUNBUFFERED=1

source /opt/software/python/anaconda/2024_02/etc/profile.d/conda.sh
conda activate mace

echo "DATE: $(date -Is)"
echo "NODE: $(hostname)"
echo "PYTHON: $(which python)"
python --version

echo
echo "Dumping mace_run_train --help ..."
mace_run_train --help > mace_help_full.txt 2>&1

echo
echo "Filtered flags:"
grep -Ei "energy_weight|forces_weight|weight|freeze|lora|multihead|replay|foundation|head|loss" mace_help_full.txt > mace_help_flags.txt || true

cat mace_help_flags.txt
