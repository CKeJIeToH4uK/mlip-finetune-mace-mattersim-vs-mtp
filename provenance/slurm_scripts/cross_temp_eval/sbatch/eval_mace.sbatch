#!/bin/bash
#SBATCH -J eval_mace
#SBATCH -A <SLURM_ACCOUNT>
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gpus=1
#SBATCH --time=01:00:00
#SBATCH -o /home/brmannanov/coursework/cross_temp_eval/slurm_logs/%x_%j.out

set -euo pipefail

source /opt/software/python/anaconda/2024_02/etc/profile.d/conda.sh
conda activate mace

BASE="/home/brmannanov/coursework"
SCRIPT="$BASE/cross_temp_eval/scripts/eval_trained_mace.py"

python "$SCRIPT" \
  --model_path "$MODEL" \
  --test_path "$TEST" \
  --output_json "$OUT" \
  --dataset_name "$DATASET"