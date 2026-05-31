#!/bin/bash
#SBATCH -J mtp16_train
#SBATCH -A <SLURM_ACCOUNT>
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --time=04:00:00
#SBATCH -o /home/brmannanov/coursework/mtp_runs/level16_run1/slurm_%j.out

set -euo pipefail

BASE="/home/brmannanov/coursework"
SCRIPT="$BASE/mtp_runs/scripts/mtp16_train_save.py"

cd "$BASE"

source ~/mlip4_env.sh
export PYTHONNOUSERSITE=1

python -c "import sys; print(sys.executable)"
python -c "import mlip_4; print(mlip_4.__file__)"

python "$SCRIPT"