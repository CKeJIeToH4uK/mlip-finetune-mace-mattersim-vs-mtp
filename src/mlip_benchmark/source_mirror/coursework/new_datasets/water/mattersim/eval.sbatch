#!/bin/bash
#SBATCH -J water_msim_eval
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
conda activate mlip-4

BASE="~/coursework/new_datasets"
SCRIPT="$BASE/water/mattersim/eval.py"

# After training, best model will be here
MODEL="$BASE/water/mattersim/finetune_result/best_model.pth"
VALID="$BASE/water/convert/valid_H2O.xyz"
TRAIN="$BASE/water/convert/train_H2O.xyz"

python "$SCRIPT" \
  --model_path "$MODEL" \
  --test_path "$VALID" \
  --output_json "$BASE/water/mattersim/eval_valid.json" \
  --dataset_name "water_valid"

python "$SCRIPT" \
  --model_path "$MODEL" \
  --test_path "$TRAIN" \
  --output_json "$BASE/water/mattersim/eval_train.json" \
  --dataset_name "water_train"
