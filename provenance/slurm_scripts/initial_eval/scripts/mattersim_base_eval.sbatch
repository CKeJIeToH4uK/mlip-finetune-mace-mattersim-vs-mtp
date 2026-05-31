#!/bin/bash
#SBATCH -J ms_base_eval
#SBATCH -A <SLURM_ACCOUNT>
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gpus=1
#SBATCH --time=01:00:00
#SBATCH -o /home/brmannanov/coursework/initial_eval/slurm_logs/%x_%j.out

set -euo pipefail

source ~/mlip4_env.sh
source /opt/software/python/anaconda/2024_02/etc/profile.d/conda.sh

BASE="/home/brmannanov/coursework"
SCRIPT="$BASE/initial_eval/scripts/mattersim_base_eval.py"

cd "$BASE"
python "$SCRIPT"
