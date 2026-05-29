#!/bin/bash
#SBATCH -J alloy_mace_lr0p001_eval
#SBATCH -A proj_1786
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --gpus=1
#SBATCH --time=02:00:00
#SBATCH -o %x_%j.out

set -euo pipefail

export PYTHONUNBUFFERED=1

source /opt/software/python/anaconda/2024_02/etc/profile.d/conda.sh
conda activate mace

BASE="~/coursework/new_datasets"
RUN_DIR="$BASE/alloy/mace_retrain_lr0p001_20260508"
RUN_NAME="alloy_ft_lr0p001"

SCRIPT="$RUN_DIR/eval_mace_alloy.py"

TRAIN="$BASE/alloy/convert/train_alloy.xyz"
VALID="$BASE/alloy/convert/valid_alloy.xyz"

MODEL=""

for candidate in \
  "$RUN_DIR/checkpoints/${RUN_NAME}_run-42.model" \
  "$RUN_DIR/models/${RUN_NAME}.model" \
  "$RUN_DIR/models/${RUN_NAME}_compiled.model" \
  "$RUN_DIR/${RUN_NAME}.model" \
  "$RUN_DIR/${RUN_NAME}_compiled.model"
do
  if [ -f "$candidate" ]; then
    MODEL="$candidate"
    break
  fi
done

if [ -z "$MODEL" ]; then
  echo "ERROR: model file not found"
  echo "Checked common candidates."
  echo
  echo "Available model-like files:"
  find "$RUN_DIR" -maxdepth 4 -type f \( -name "*.model" -o -name "*.pt" -o -name "*.pth" \) | sort || true
  exit 1
fi

echo "Using model: $MODEL"

python "$SCRIPT" \
  --model_path "$MODEL" \
  --test_path "$VALID" \
  --output_json "$RUN_DIR/eval_valid.json" \
  --dataset_name "alloy_valid_lr0p001"

python "$SCRIPT" \
  --model_path "$MODEL" \
  --test_path "$TRAIN" \
  --output_json "$RUN_DIR/eval_train.json" \
  --dataset_name "alloy_train_lr0p001"
