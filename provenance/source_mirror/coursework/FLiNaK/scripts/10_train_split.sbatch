#!/bin/bash
#SBATCH -J ms_flinak_split
#SBATCH -p normal
#SBATCH -A proj_1786
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gpus=1
#SBATCH --time=10:00:00
#SBATCH -o logs/%x_%j.out

# Вариант B: 90/10 split. Для себя / курсача — честная валидация,
# чтобы видеть обобщение, а не только запоминание.

set -euo pipefail
mkdir -p logs

CPUS="${SLURM_CPUS_PER_TASK:-8}"
GPUS="${SLURM_GPUS_ON_NODE:-1}"
export OMP_NUM_THREADS="$CPUS"
export MKL_NUM_THREADS="$CPUS"
export PYTHONUNBUFFERED=1

source /opt/software/python/anaconda/2024_02/etc/profile.d/conda.sh
conda activate mlip-4

BASE="~/coursework/FLiNaK"
TRAIN="$BASE/data/train_90.xyz"
VALID="$BASE/data/valid_10.xyz"

RUN_DIR="$BASE/run_split/${SLURM_JOB_ID}"
mkdir -p "$RUN_DIR"

{
  echo "DATE: $(date -Is)"
  echo "JOBID: ${SLURM_JOB_ID}"
  echo "NODELIST: ${SLURM_NODELIST}"
  echo "CPUS_PER_TASK: $CPUS"
  echo "GPUS_ON_NODE:  $GPUS"
  python -c "import torch; print('torch', torch.__version__, 'cuda', torch.cuda.is_available()); \
             print('gpu_name', torch.cuda.get_device_name(0) if torch.cuda.is_available() else None)"
  echo "nvidia-smi:"
  nvidia-smi || true
} > "$RUN_DIR/resources.txt" 2>&1

FT_SCRIPT="~/.conda/envs/mlip-4/lib/python3.11/site-packages/mattersim/training/finetune_mattersim.py"

export WANDB_MODE=offline
export WANDB_DIR="$RUN_DIR/wandb"

# уникальный порт, чтобы два torchrun на одной ноде не дрались за 29500
MASTER_PORT=$((29500 + SLURM_JOB_ID % 10000))

{
time torchrun --nproc_per_node=1 --master_port="$MASTER_PORT" "$FT_SCRIPT" \
  --run_name "ft_split" \
  --load_model_path mattersim-v1.0.0-1m \
  --train_data_path "$TRAIN" \
  --valid_data_path "$VALID" \
  --device cuda \
  --cutoff 5.0 \
  --threebody_cutoff 4.0 \
  --batch_size 32 \
  --lr 5e-5 \
  --step_size 200 \
  --epochs 500 \
  --early_stop_patience 100 \
  --seed 42 \
  --save_path "$RUN_DIR/finetune_result" \
  --save_checkpoint \
  --ckpt_interval 50 \
  --include_forces \
  --re_normalize
} 2>&1 | tee "$RUN_DIR/train.log"
