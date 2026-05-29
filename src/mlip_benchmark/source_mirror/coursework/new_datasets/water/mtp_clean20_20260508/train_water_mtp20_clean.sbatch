#!/bin/bash
#SBATCH -J water_mtp20_clean
#SBATCH -A proj_1786
#SBATCH -N 1
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1
#SBATCH --time=10:00:00
#SBATCH -o %x_%j.out

set -euo pipefail

source ~/mlip4_env.sh
export PYTHONNOUSERSITE=1
export PYTHONUNBUFFERED=1

BASE="~/coursework/new_datasets"
RUN_DIR="$BASE/water/mtp_clean20_20260508"
SCRIPT="$RUN_DIR/train_water_mtp20_clean.py"
NPROC="${SLURM_NTASKS:-8}"

mkdir -p "$RUN_DIR"

{
  echo "DATE: $(date -Is)"
  echo "JOBID: ${SLURM_JOB_ID:-}"
  echo "NODELIST: ${SLURM_NODELIST:-}"
  echo "NTASKS: ${SLURM_NTASKS:-8}"
  echo "CPUS_PER_TASK: ${SLURM_CPUS_PER_TASK:-1}"

  echo
  echo "Input JSON files:"
  ls -lh "$BASE/water/convert/train_H2O.json"
  ls -lh "$BASE/water/convert/valid_H2O.json"

  echo
  echo "Script:"
  ls -lh "$SCRIPT"

  echo
  echo "Python:"
  which python
  python --version

  echo
  echo "MPI command:"
  echo "mpirun -np ${NPROC} python ${SCRIPT}"
} > "$RUN_DIR/resources.txt" 2>&1

echo "mpirun --bind-to none --map-by slot -np ${NPROC} python ${SCRIPT}" > "$RUN_DIR/exact_command.txt"

cd "$RUN_DIR"

mpirun --bind-to none --map-by slot -np "$NPROC" python "$SCRIPT" 2>&1 | tee "$RUN_DIR/train.log"
