#!/bin/bash
#SBATCH -J ms_sweep
#SBATCH -p normal
#SBATCH -A proj_1786
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gpus=1
#SBATCH --time=08:00:00
#SBATCH -o logs/%x_%j.out
#SBATCH -o logs/%x_%j.out

set -euo pipefail
mkdir -p logs

source /opt/software/python/anaconda/2024_02/etc/profile.d/conda.sh
conda activate mlip-4

# параметры из sbatch
LR=${LR}
BS=${BS}

TRAIN="~/coursework/databases/train_300K.xyz"
VALID="~/coursework/databases/test_300K.xyz"

BASE="~/coursework/mattersim_finetune/sweep_lr_bs"
RUN_DIR="${BASE}/runs/lr${LR}_bs${BS}"
mkdir -p "$RUN_DIR"

FT_SCRIPT="~/.conda/envs/mlip-4/lib/python3.11/site-packages/mattersim/training/finetune_mattersim.py"

{
  torchrun --nproc_per_node=1 "$FT_SCRIPT" \
    --run_name "lr${LR}_bs${BS}" \
    --load_model_path mattersim-v1.0.0-1m \
    --train_data_path "$TRAIN" \
    --valid_data_path "$VALID" \
    --device cuda \
    --batch_size "$BS" \
    --lr "$LR" \
    --epochs 500 \
    --step_size 100 \
    --seed 42 \
    --save_path "$RUN_DIR" \
    --include_forces \
    --early_stop_patience 999999 \
    --re_normalize
} 2>&1 | tee "$RUN_DIR/train.log"