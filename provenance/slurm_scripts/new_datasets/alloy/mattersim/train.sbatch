#!/bin/bash
#SBATCH -J alloy_msim
#SBATCH -A <SLURM_ACCOUNT>
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

BASE="/home/brmannanov/coursework/new_datasets"
TRAIN="$BASE/alloy/convert/train_alloy.xyz"
VALID="$BASE/alloy/convert/valid_alloy.xyz"

RUN_DIR="$BASE/alloy/mattersim"
mkdir -p "$RUN_DIR"

{
  echo "DATE: $(date -Is)"
  echo "JOBID: ${SLURM_JOB_ID}"
  echo "NODELIST: ${SLURM_NODELIST}"
  python -c "import torch; print('torch', torch.__version__, 'cuda', torch.cuda.is_available()); \
             print('gpu_name', torch.cuda.get_device_name(0) if torch.cuda.is_available() else None)"
  nvidia-smi || true
} > "$RUN_DIR/resources.txt" 2>&1

FT_SCRIPT="/home/brmannanov/.conda/envs/mlip-4/lib/python3.11/site-packages/mattersim/training/finetune_mattersim.py"

export WANDB_MODE=offline
export WANDB_DIR="$RUN_DIR/wandb"

# Variable-size configs (2-252 atoms), batch_size=4 to be safe for largest configs
{
time torchrun --nproc_per_node=1 --master_port=29501 "$FT_SCRIPT" \
  --run_name "alloy_ft" \
  --load_model_path mattersim-v1.0.0-5m \
  --train_data_path "$TRAIN" \
  --valid_data_path "$VALID" \
  --device cuda \
  --cutoff 5.0 \
  --threebody_cutoff 4.0 \
  --batch_size 4 \
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
