#!/bin/bash
set -euo pipefail

source ~/mlip4_env.sh

cd "$SLURM_SUBMIT_DIR"

mpirun -np "$SLURM_NTASKS" python mtp.py
