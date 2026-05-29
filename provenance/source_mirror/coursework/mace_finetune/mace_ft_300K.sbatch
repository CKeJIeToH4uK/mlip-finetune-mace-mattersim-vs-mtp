#!/bin/bash
#SBATCH -J mace_ft_300K
#SBATCH -A proj_1786
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gpus=1
#SBATCH --time=08:00:00
#SBATCH -o logs/%x_%j.out

set -euo pipefail

mkdir -p logs

CPUS="${SLURM_CPUS_PER_TASK:-8}"
GPUS="${SLURM_GPUS_ON_NODE:-1}"
export OMP_NUM_THREADS="$CPUS"
export MKL_NUM_THREADS="$CPUS"
export PYTHONUNBUFFERED=1

source /opt/software/python/anaconda/2024_02/etc/profile.d/conda.sh
conda activate mace

BASE="~/coursework"
TRAIN="$BASE/databases/train_300K.xyz"
TEST="$BASE/databases/test_300K.xyz"

RUN_DIR="$BASE/mace_finetune/ft_300K"
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

cd "$RUN_DIR"

# ---- запуск обучения ----
{
time mace_run_train \
  --name=ft_300K \
  --foundation_model="~/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model" \
  --multiheads_finetuning=False \
  --train_file="$TRAIN" \
  --test_file="$TEST" \
  --valid_fraction=0.05 \
  --energy_key=energy \
  --forces_key=forces \
  --atomic_numbers="[1,6,7,8]" \
  --E0s=average \
  --scaling=rms_forces_scaling \
  --batch_size=32 \
  --lr=0.01 \
  --max_num_epochs=500 \
  --patience=200 \
  --device=cuda \
  --seed=42
} 2>&1 | tee "$RUN_DIR/train.log"