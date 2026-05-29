#!/bin/bash
#SBATCH -J ms_flinak_eval
#SBATCH -p normal
#SBATCH -A proj_1786
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --gpus=1
#SBATCH --time=00:30:00
#SBATCH -o logs/%x_%j.out

# Стадия 2: универсальный eval MatterSim.
# Принимает через --export:
#   MODEL_PATH   путь к .pth или "default" (zero-shot базовая MatterSim)
#   TEST_PATH    xyz-файл для eval
#   OUT_JSON     куда писать json с метриками
#   DATASET_NAME (опционально) имя для лога
#
# Примеры запуска (после того как тренинги закончились):
#
#   # zero-shot на всех 754
#   sbatch --export=ALL,MODEL_PATH=default,\
# TEST_PATH=~/coursework/FLiNaK/data/train_all.xyz,\
# OUT_JSON=~/coursework/FLiNaK/eval/zero_shot_all.json,\
# DATASET_NAME=all \
#     20_eval.sbatch
#
#   # FT вариант A на всех 754
#   sbatch --export=ALL,MODEL_PATH=~/coursework/FLiNaK/run_all/<JOBID>/finetune_result/best_model.pth,\
# TEST_PATH=~/coursework/FLiNaK/data/train_all.xyz,\
# OUT_JSON=~/coursework/FLiNaK/eval/ft_all_on_all.json,\
# DATASET_NAME=all \
#     20_eval.sbatch
#
#   # FT вариант B на valid (честная цифра обобщения)
#   sbatch --export=ALL,MODEL_PATH=~/coursework/FLiNaK/run_split/<JOBID>/finetune_result/best_model.pth,\
# TEST_PATH=~/coursework/FLiNaK/data/valid_10.xyz,\
# OUT_JSON=~/coursework/FLiNaK/eval/ft_split_on_valid.json,\
# DATASET_NAME=valid \
#     20_eval.sbatch

set -euo pipefail
mkdir -p logs

: "${MODEL_PATH:?need MODEL_PATH}"
: "${TEST_PATH:?need TEST_PATH}"
: "${OUT_JSON:?need OUT_JSON}"
DATASET_NAME="${DATASET_NAME:-unnamed}"

CPUS="${SLURM_CPUS_PER_TASK:-4}"
export OMP_NUM_THREADS="$CPUS"
export MKL_NUM_THREADS="$CPUS"
export PYTHONUNBUFFERED=1

source /opt/software/python/anaconda/2024_02/etc/profile.d/conda.sh
conda activate mlip-4

EVAL_SCRIPT="~/coursework/cross_temp_eval/scripts/eval_trained_mattersim.py"

mkdir -p "$(dirname "$OUT_JSON")"

python "$EVAL_SCRIPT" \
  --model_path "$MODEL_PATH" \
  --test_path "$TEST_PATH" \
  --output_json "$OUT_JSON" \
  --dataset_name "$DATASET_NAME"
