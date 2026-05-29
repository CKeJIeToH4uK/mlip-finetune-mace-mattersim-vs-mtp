#!/bin/bash
#SBATCH -J mtp20_train
#SBATCH -A proj_1786
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --time=04:00:00
#SBATCH -o ~/coursework/mtp_runs/level20_run1/slurm_%j.out

set -euo pipefail

BASE="~/coursework"
SCRIPT="$BASE/mtp_runs/scripts/mtp20_train_save.py"

cd "$BASE"

source ~/mlip4_env.sh
export PYTHONNOUSERSITE=1

python -c "import sys; print(sys.executable)"
python -c "import mlip_4; print(mlip_4.__file__)"

python "$SCRIPT"