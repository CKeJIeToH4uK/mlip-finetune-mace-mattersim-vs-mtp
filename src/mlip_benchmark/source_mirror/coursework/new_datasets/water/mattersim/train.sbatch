#!/bin/bash
#SBATCH -J water_msim
#SBATCH -A proj_1786
#SBATCH -p normal
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gpus=1
#SBATCH --time=08:00:00
#SBATCH -o %x_%j.out

set -euo pipefail

CPUS="${SLURM_CPUS_PER_TASK:-8}"
export OMP_NUM_THREADS="$CPUS"
export MKL_NUM_THREADS="$CPUS"
export PYTHONUNBUFFERED=1

source /opt/software/python/anaconda/2024_02/etc/profile.d/conda.sh
conda activate mlip-4

BASE="~/coursework/new_datasets"
TRAIN="$BASE/water/convert/train_H2O.xyz"
VALID="$BASE/water/convert/valid_H2O.xyz"

RUN_DIR="$BASE/water/mattersim"
mkdir -p "$RUN_DIR"

{
  echo "DATE: $(date -Is)"
  echo "JOBID: ${SLURM_JOB_ID}"
  echo "NODELIST: ${SLURM_NODELIST}"
  python -c "import torch; print('torch', torch.__version__, 'cuda', torch.cuda.is_available()); \
             print('gpu_name', torch.cuda.get_device_name(0) if torch.cuda.is_available() else None)"
  nvidia-smi || true
} > "$RUN_DIR/resources.txt" 2>&1

FT_SCRIPT="~/.conda/envs/mlip-4/lib/python3.11/site-packages/mattersim/training/finetune_mattersim.py"

export WANDB_MODE=offline
export WANDB_DIR="$RUN_DIR/wandb"

{
time torchrun --nproc_per_node=1 "$FT_SCRIPT" \
  --run_name "water_ft" \
  --load_model_path mattersim-v1.0.0-1m \
  --train_data_path "$TRAIN" \
  --valid_data_path "$VALID" \
  --device cuda \
  --cutoff 5.0 \
  --threebody_cutoff 4.0 \
  --batch_size 8 \
  --lr 5e-5 \
  --step_size 50 \
  --epochs 200 \
  --seed 42 \
  --save_path "$RUN_DIR/finetune_result" \
  --save_checkpoint \
  --ckpt_interval 25 \
  --include_forces \
  --early_stop_patience 50 \
  --re_normalize
} 2>&1 | tee "$RUN_DIR/train.log"
