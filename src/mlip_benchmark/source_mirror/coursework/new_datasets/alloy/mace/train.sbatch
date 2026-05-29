#!/bin/bash
#SBATCH -J alloy_mace
#SBATCH -A proj_1786
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
conda activate mace

BASE="~/coursework/new_datasets"
TRAIN="$BASE/alloy/convert/train_alloy.xyz"
VALID="$BASE/alloy/convert/valid_alloy.xyz"

RUN_DIR="$BASE/alloy/mace"
mkdir -p "$RUN_DIR"

{
  echo "DATE: $(date -Is)"
  echo "JOBID: ${SLURM_JOB_ID}"
  echo "NODELIST: ${SLURM_NODELIST}"
  python -c "import torch; print('torch', torch.__version__, 'cuda', torch.cuda.is_available()); \
             print('gpu_name', torch.cuda.get_device_name(0) if torch.cuda.is_available() else None)"
  nvidia-smi || true
} > "$RUN_DIR/resources.txt" 2>&1

cd "$RUN_DIR"

# Variable-size configs (2-252 atoms), batch_size=8 should fit in 32GB.
# If OOM on largest configs, reduce to 4.
{
time mace_run_train \
  --name=alloy_ft \
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
  --lr=0.01 \
  --max_num_epochs=200 \
  --patience=50 \
  --device=cuda \
  --seed=42
} 2>&1 | tee "$RUN_DIR/train.log"
