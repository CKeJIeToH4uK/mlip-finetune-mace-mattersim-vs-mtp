#!/bin/bash
#SBATCH -J eval_ms
#SBATCH -A proj_1786
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gpus=1
#SBATCH --time=01:00:00
#SBATCH -o ~/coursework/cross_temp_eval/slurm_logs/%x_%j.out

set -euo pipefail

source /opt/software/python/anaconda/2024_02/etc/profile.d/conda.sh
conda activate mlip-4

BASE="~/coursework"
SCRIPT="$BASE/cross_temp_eval/scripts/eval_trained_mattersim.py"

python "$SCRIPT" \
  --model_path "$MODEL" \
  --test_path "$TEST" \
  --output_json "$OUT" \
  --dataset_name "$DATASET"