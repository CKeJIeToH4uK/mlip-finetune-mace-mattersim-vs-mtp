#!/bin/bash
#SBATCH -J mtp_init_eval
#SBATCH -A <SLURM_ACCOUNT>
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --time=01:00:00
#SBATCH -o /home/brmannanov/coursework/initial_eval/slurm_logs/%x_%j.out

source ~/mlip4_env.sh

set -euo pipefail

source /opt/software/python/anaconda/2024_02/etc/profile.d/conda.sh

BASE="/home/brmannanov/coursework"
SCRIPT="$BASE/initial_eval/scripts/mtp_init_eval.py"

cd "$BASE"

python "$SCRIPT"


