#!/bin/bash
#SBATCH -J alloy_ew10_50_norm
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
conda activate mace

BASE="~/coursework/new_datasets"
PKG="$BASE/alloy/mace_ablation_normal_ew10_ew50_20260509"

TRAIN="$BASE/alloy/convert/train_alloy.xyz"
VALID="$BASE/alloy/convert/valid_alloy.xyz"
FOUNDATION="~/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model"

EVAL_SCRIPT="$PKG/eval_mace_alloy.py"

run_one() {
  local SUBDIR="$1"
  local RUN_NAME="$2"
  local ENERGY_WEIGHT="$3"
  local FORCES_WEIGHT="$4"
  local RUN_TYPE="$5"

  local RUN_DIR="$PKG/$SUBDIR"

  mkdir -p "$RUN_DIR"/{logs,results,checkpoints,models}

  {
    echo "DATE: $(date -Is)"
    echo "JOBID: ${SLURM_JOB_ID:-}"
    echo "NODELIST: ${SLURM_NODELIST:-}"
    echo "PARTITION: ${SLURM_JOB_PARTITION:-}"
    echo "CPUS_PER_TASK: $CPUS"
    echo
    echo "RUN_DIR: $RUN_DIR"
    echo "RUN_NAME: $RUN_NAME"
    echo "RUN_TYPE: $RUN_TYPE"
    echo "ENERGY_WEIGHT: $ENERGY_WEIGHT"
    echo "FORCES_WEIGHT: $FORCES_WEIGHT"
    echo
    echo "Input files:"
    ls -lh "$TRAIN" "$VALID"
    echo
    echo "Foundation model:"
    ls -lh "$FOUNDATION"
    echo
    echo "Python / torch:"
    which python
    python --version
    python -c "import torch; print('torch', torch.__version__, 'cuda', torch.cuda.is_available()); print('gpu_name', torch.cuda.get_device_name(0) if torch.cuda.is_available() else None)"
    echo
    echo "nvidia-smi:"
    nvidia-smi || true
  } > "$RUN_DIR/resources_${SLURM_JOB_ID}.txt" 2>&1

  cat > "$RUN_DIR/exact_command_${SLURM_JOB_ID}.txt" <<CMD
mace_run_train \\
  --name="$RUN_NAME" \\
  --foundation_model="$FOUNDATION" \\
  --multiheads_finetuning=False \\
  --train_file="$TRAIN" \\
  --valid_file="$VALID" \\
  --energy_key=energy \\
  --forces_key=forces \\
  --atomic_numbers="[23,41,42,73,74]" \\
  --E0s=average \\
  --scaling=rms_forces_scaling \\
  --batch_size=8 \\
  --lr=0.001 \\
  --max_num_epochs=200 \\
  --patience=50 \\
  --eval_interval=25 \\
  --loss=weighted \\
  --energy_weight="$ENERGY_WEIGHT" \\
  --forces_weight="$FORCES_WEIGHT" \\
  --save_all_checkpoints \\
  --keep_checkpoints \\
  --device=cuda \\
  --seed=42 \\
  --log_dir="$RUN_DIR/logs" \\
  --results_dir="$RUN_DIR/results" \\
  --checkpoints_dir="$RUN_DIR/checkpoints" \\
  --model_dir="$RUN_DIR/models"
CMD

  echo
  echo "============================================================"
  echo "TRAINING $RUN_TYPE"
  echo "RUN_DIR=$RUN_DIR"
  echo "============================================================"
  echo

  cd "$RUN_DIR"

  time mace_run_train \
    --name="$RUN_NAME" \
    --foundation_model="$FOUNDATION" \
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
    --max_num_epochs=200 \
    --patience=50 \
    --eval_interval=25 \
    --loss=weighted \
    --energy_weight="$ENERGY_WEIGHT" \
    --forces_weight="$FORCES_WEIGHT" \
    --save_all_checkpoints \
    --keep_checkpoints \
    --device=cuda \
    --seed=42 \
    --log_dir="$RUN_DIR/logs" \
    --results_dir="$RUN_DIR/results" \
    --checkpoints_dir="$RUN_DIR/checkpoints" \
    --model_dir="$RUN_DIR/models" \
    2>&1 | tee "$RUN_DIR/train_${SLURM_JOB_ID}.log"

  ln -sfn "train_${SLURM_JOB_ID}.log" "$RUN_DIR/train.log"

  local MODEL=""

  for candidate in \
    "$RUN_DIR/checkpoints/${RUN_NAME}_run-42.model" \
    "$RUN_DIR/models/${RUN_NAME}.model" \
    "$RUN_DIR/models/${RUN_NAME}_compiled.model" \
    "$RUN_DIR/${RUN_NAME}.model" \
    "$RUN_DIR/${RUN_NAME}_compiled.model"
  do
    if [ -f "$candidate" ]; then
      MODEL="$candidate"
      break
    fi
  done

  if [ -z "$MODEL" ]; then
    echo "ERROR: model file not found for $RUN_TYPE"
    find "$RUN_DIR" -maxdepth 4 -type f \( -name "*.model" -o -name "*.pt" -o -name "*.pth" \) | sort || true
    exit 1
  fi

  echo
  echo "============================================================"
  echo "EVAL $RUN_TYPE"
  echo "MODEL=$MODEL"
  echo "============================================================"
  echo

  python "$EVAL_SCRIPT" \
    --model_path "$MODEL" \
    --train_path "$TRAIN" \
    --valid_path "$VALID" \
    --out_dir "$RUN_DIR" \
    --run_type "$RUN_TYPE" \
    2>&1 | tee "$RUN_DIR/eval_${SLURM_JOB_ID}.log"
}

run_one "full_ew10_normal" "alloy_mace_full_ew10_normal" "10" "100" "full_ew10_normal"
run_one "full_ew50_normal" "alloy_mace_full_ew50_normal" "50" "100" "full_ew50_normal"

echo
echo "DONE: EW10 and EW50 normal runs finished."
