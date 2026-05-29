#!/bin/bash
#SBATCH -J eval_mtp
#SBATCH -A proj_1786
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --time=01:00:00
#SBATCH -o ~/coursework/cross_temp_eval/slurm_logs/%x_%j.out

set -euo pipefail

BASE="~/coursework"
SCRIPT="$BASE/cross_temp_eval/scripts/eval_trained_mtp.py"

cd "$BASE"

source ~/mlip4_env.sh
export PYTHONNOUSERSITE=1

python "$SCRIPT" \
  --model_path "$MODEL" \
  --test_path "$TEST" \
  --output_json "$OUT" \
  --dataset_name "$DATASET" \
  --model_name "$MODEL_NAME"