#!/bin/bash
#SBATCH -J mace_base_eval
#SBATCH -A proj_1786
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gpus=1
#SBATCH --time=01:00:00
#SBATCH -o ~/coursework/initial_eval/slurm_logs/%x_%j.out

set -euo pipefail

source /opt/software/python/anaconda/2024_02/etc/profile.d/conda.sh
conda activate mace

BASE="~/coursework"
SCRIPT="$BASE/initial_eval/scripts/mace_base_eval.py"

cd "$BASE"
python "$SCRIPT"
