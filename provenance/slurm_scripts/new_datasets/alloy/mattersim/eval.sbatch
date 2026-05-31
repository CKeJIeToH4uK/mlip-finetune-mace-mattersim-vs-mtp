#!/bin/bash
#SBATCH -J alloy_msim_eval
#SBATCH -A <SLURM_ACCOUNT>
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

BASE="/home/brmannanov/coursework/new_datasets"
SCRIPT="$BASE/alloy/mattersim/eval.py"

MODEL="$BASE/alloy/mattersim/finetune_result/best_model.pth"
VALID="$BASE/alloy/convert/valid_alloy.xyz"
TRAIN="$BASE/alloy/convert/train_alloy.xyz"

python "$SCRIPT" \
  --model_path "$MODEL" \
  --test_path "$VALID" \
  --output_json "$BASE/alloy/mattersim/eval_valid.json" \
  --dataset_name "alloy_valid"

python "$SCRIPT" \
  --model_path "$MODEL" \
  --test_path "$TRAIN" \
  --output_json "$BASE/alloy/mattersim/eval_train.json" \
  --dataset_name "alloy_train"
