#!/bin/bash
#SBATCH -J alloy_protocols_norm
#SBATCH -A <SLURM_ACCOUNT>
#SBATCH -p normal
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gpus=1
#SBATCH --time=08:00:00
#SBATCH -o %x_%j.out

set -uo pipefail

CPUS="${SLURM_CPUS_PER_TASK:-8}"
JOB_ID="${SLURM_JOB_ID:-manual}"

export OMP_NUM_THREADS="$CPUS"
export MKL_NUM_THREADS="$CPUS"
export PYTHONUNBUFFERED=1

source /opt/software/python/anaconda/2024_02/etc/profile.d/conda.sh
conda activate mace

BASE="/home/brmannanov/coursework/new_datasets"
PKG="$BASE/alloy/mace_ablation_normal_protocols_20260509"

TRAIN="$BASE/alloy/convert/train_alloy.xyz"
VALID="$BASE/alloy/convert/valid_alloy.xyz"
FOUNDATION="/home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model"
EVAL_SCRIPT="$PKG/eval_mace_alloy.py"
STATUS_FILE="$PKG/run_status_${JOB_ID}.tsv"

mkdir -p "$PKG"
printf "run_type\tstatus\texit_code\tnote\n" > "$STATUS_FILE"

record_status() {
  local RUN_TYPE="$1"
  local STATUS="$2"
  local EXIT_CODE="$3"
  local NOTE="$4"
  printf "%s\t%s\t%s\t%s\n" "$RUN_TYPE" "$STATUS" "$EXIT_CODE" "$NOTE" >> "$STATUS_FILE"
}

find_model() {
  local RUN_DIR="$1"
  local RUN_NAME="$2"
  local candidate

  for candidate in \
    "$RUN_DIR/checkpoints/${RUN_NAME}_run-42.model" \
    "$RUN_DIR/models/${RUN_NAME}.model" \
    "$RUN_DIR/models/${RUN_NAME}_compiled.model" \
    "$RUN_DIR/${RUN_NAME}.model" \
    "$RUN_DIR/${RUN_NAME}_compiled.model"
  do
    if [ -f "$candidate" ]; then
      echo "$candidate"
      return 0
    fi
  done

  echo "Available model-like files:" >&2
  find "$RUN_DIR" -maxdepth 4 -type f \( -name "*.model" -o -name "*.pt" -o -name "*.pth" \) | sort >&2 || true
  return 1
}

run_one() {
  local SUBDIR="$1"
  local RUN_NAME="$2"
  local RUN_TYPE="$3"
  shift 3
  local EXTRA_FLAGS=("$@")
  local RUN_DIR="$PKG/$SUBDIR"
  local TRAIN_RC
  local EVAL_RC
  local MODEL

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
    echo "EXTRA_FLAGS: ${EXTRA_FLAGS[*]}"
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
  } > "$RUN_DIR/resources_${JOB_ID}.txt" 2>&1

  {
    cat <<CMD
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
CMD
    for flag in "${EXTRA_FLAGS[@]}"; do
      printf '  %s \\\n' "$flag"
    done
    cat <<CMD
  --save_all_checkpoints \\
  --keep_checkpoints \\
  --device=cuda \\
  --seed=42 \\
  --log_dir="$RUN_DIR/logs" \\
  --results_dir="$RUN_DIR/results" \\
  --checkpoints_dir="$RUN_DIR/checkpoints" \\
  --model_dir="$RUN_DIR/models"
CMD
  } > "$RUN_DIR/exact_command_${JOB_ID}.txt"

  echo
  echo "============================================================"
  echo "TRAINING $RUN_TYPE"
  echo "RUN_DIR=$RUN_DIR"
  echo "============================================================"
  echo

  cd "$RUN_DIR" || {
    record_status "$RUN_TYPE" "train_failed" "1" "could_not_cd_to_run_dir"
    return 0
  }

  {
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
      "${EXTRA_FLAGS[@]}" \
      --save_all_checkpoints \
      --keep_checkpoints \
      --device=cuda \
      --seed=42 \
      --log_dir="$RUN_DIR/logs" \
      --results_dir="$RUN_DIR/results" \
      --checkpoints_dir="$RUN_DIR/checkpoints" \
      --model_dir="$RUN_DIR/models"
  } 2>&1 | tee "$RUN_DIR/train_${JOB_ID}.log"
  TRAIN_RC=${PIPESTATUS[0]}

  ln -sfn "train_${JOB_ID}.log" "$RUN_DIR/train.log"

  if [ "$TRAIN_RC" -ne 0 ]; then
    record_status "$RUN_TYPE" "train_failed" "$TRAIN_RC" "mace_run_train_failed"
    return 0
  fi

  if ! MODEL="$(find_model "$RUN_DIR" "$RUN_NAME")"; then
    record_status "$RUN_TYPE" "model_missing" "1" "model_file_not_found_after_training"
    return 0
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
    2>&1 | tee "$RUN_DIR/eval_${JOB_ID}.log"
  EVAL_RC=${PIPESTATUS[0]}

  if [ "$EVAL_RC" -ne 0 ]; then
    record_status "$RUN_TYPE" "eval_failed" "$EVAL_RC" "eval_script_failed"
    return 0
  fi

  record_status "$RUN_TYPE" "ok" "0" "train_and_eval_finished"
}

run_one "stage2_normal" "alloy_mace_stage2_normal" "stage2_normal" \
  "--energy_weight=1" \
  "--forces_weight=100" \
  "--swa" \
  "--start_swa=150" \
  "--swa_lr=0.0003" \
  "--swa_energy_weight=1000" \
  "--swa_forces_weight=100"

run_one "lora_ew10_normal" "alloy_mace_lora_ew10_normal" "lora_ew10_normal" \
  "--energy_weight=10" \
  "--forces_weight=100" \
  "--lora=True" \
  "--lora_rank=4" \
  "--lora_alpha=1.0"

run_one "freeze1_ew10_normal" "alloy_mace_freeze1_ew10_normal" "freeze1_ew10_normal" \
  "--energy_weight=10" \
  "--forces_weight=100" \
  "--freeze=1"

echo
echo "DONE: protocols normal package finished attempts."
echo "Status file: $STATUS_FILE"
cat "$STATUS_FILE"
