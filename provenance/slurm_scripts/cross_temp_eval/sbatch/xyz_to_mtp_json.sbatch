#!/bin/bash
#SBATCH -J xyz2mtpjson
#SBATCH -A <SLURM_ACCOUNT>
#SBATCH -N 1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=00:30:00
#SBATCH -o /home/brmannanov/coursework/cross_temp_eval/slurm_logs/%x_%j.out

set -euo pipefail

BASE="/home/brmannanov/coursework"
SCRIPT="$BASE/cross_temp_eval/scripts/xyz_to_mtp_json.py"

cd "$BASE"

source ~/mlip4_env.sh
export PYTHONNOUSERSITE=1

python "$SCRIPT" \
  --input_xyz "$INPUT_XYZ" \
  --output_json "$OUTPUT_JSON"
