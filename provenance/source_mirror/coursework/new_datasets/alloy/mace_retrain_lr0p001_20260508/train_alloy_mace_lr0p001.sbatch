#!/bin/bash
#SBATCH -J alloy_mace_lr0p001
#SBATCH -A proj_1786
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gpus=1
#SBATCH --time=08:00:00
#SBATCH -o %x_%j.out

set -euo pipefail

CPUS="${SLURM_CPUS_PER_TASK:-8}"
GPUS="${SLURM_GPUS_ON_NODE:-1}"

export OMP_NUM_THREADS="$CPUS"
export MKL_NUM_THREADS="$CPUS"
export PYTHONUNBUFFERED=1

source /opt/software/python/anaconda/2024_02/etc/profile.d/conda.sh
conda activate mace

BASE="~/coursework/new_datasets"

TRAIN="$BASE/alloy/convert/train_alloy.xyz"
VALID="$BASE/alloy/convert/valid_alloy.xyz"

RUN_DIR="$BASE/alloy/mace_retrain_lr0p001_20260508"
RUN_NAME="alloy_ft_lr0p001"

mkdir -p "$RUN_DIR"/{logs,results,checkpoints,models}

{
  echo "DATE: $(date -Is)"
  echo "JOBID: ${SLURM_JOB_ID:-}"
  echo "NODELIST: ${SLURM_NODELIST:-}"
  echo "CPUS_PER_TASK: $CPUS"
  echo "GPUS_ON_NODE: $GPUS"

  echo
  echo "Input files:"
  ls -lh "$TRAIN" "$VALID"

  echo
  python -c "import torch; print('torch', torch.__version__, 'cuda', torch.cuda.is_available()); print('gpu_name', torch.cuda.get_device_name(0) if torch.cuda.is_available() else None)"

  echo
  echo "nvidia-smi:"
  nvidia-smi || true
} > "$RUN_DIR/resources.txt" 2>&1

cd "$RUN_DIR"

time mace_run_train \
  --name="$RUN_NAME" \
  --foundation_model="~/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model" \
  --multiheads_finetuning=False \
  --train_file="$TRAIN" \
  --valid_file="$VALID" \
  --energy_key=energy \
  --forces_key=forces \
  --atomic_numbers="[23,41,42,73,74]" \
  --E0s=average \
  --scaling=rms_forces_scaling \
  --batch_size=8 \
  --lr=0.001 \
  --max_num_epochs=500 \
  --patience=200 \
  --eval_interval=25 \
  --save_all_checkpoints \
  --keep_checkpoints \
  --device=cuda \
  --seed=42 \
  --log_dir="$RUN_DIR/logs" \
  --results_dir="$RUN_DIR/results" \
  --checkpoints_dir="$RUN_DIR/checkpoints" \
  --model_dir="$RUN_DIR/models" \
  2>&1 | tee "$RUN_DIR/train.log"
