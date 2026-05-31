#!/bin/bash
#SBATCH -J alloy_mace_fair_eval
#SBATCH -A <SLURM_ACCOUNT>
#SBATCH -p gpu-ef-quick
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --gpus=1
#SBATCH --time=00:30:00
#SBATCH -o %x_%j.out

set -euo pipefail

export PYTHONUNBUFFERED=1

source /opt/software/python/anaconda/2024_02/etc/profile.d/conda.sh
conda activate mace

BASE="/home/brmannanov/coursework/new_datasets"
RUN_DIR="$BASE/alloy/mace_retrain_lr0p001_fair200_quick3h_20260509"
RUN_NAME="alloy_ft_lr0p001_fair200"

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
  echo
  echo "Available model-like files:"
  find "$RUN_DIR" -maxdepth 4 -type f \( -name "*.model" -o -name "*.pt" -o -name "*.pth" \) | sort || true
  exit 1
fi

echo "Using model: $MODEL"

python "$SCRIPT" \
  --model_path "$MODEL" \
  --train_path "$TRAIN" \
  --valid_path "$VALID" \
  --out_dir "$RUN_DIR"
