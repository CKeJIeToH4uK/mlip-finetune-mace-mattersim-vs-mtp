#!/bin/bash
#SBATCH -J water_mace_eval
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
conda activate mace

BASE="/home/brmannanov/coursework/new_datasets"
SCRIPT="$BASE/water/mace/eval.py"

# After training, the model will be at water_ft.model
MODEL="$BASE/water/mace/water_ft.model"
VALID="$BASE/water/convert/valid_H2O.xyz"
TRAIN="$BASE/water/convert/train_H2O.xyz"

python "$SCRIPT" \
  --model_path "$MODEL" \
  --test_path "$VALID" \
  --output_json "$BASE/water/mace/eval_valid.json" \
  --dataset_name "water_valid"

python "$SCRIPT" \
  --model_path "$MODEL" \
  --test_path "$TRAIN" \
  --output_json "$BASE/water/mace/eval_train.json" \
  --dataset_name "water_train"
