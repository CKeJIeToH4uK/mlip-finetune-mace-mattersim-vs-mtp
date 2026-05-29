#!/bin/bash
#SBATCH -J water_mtp20
#SBATCH -A proj_1786
#SBATCH -N 1
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1
#SBATCH --time=08:00:00
#SBATCH -o %x_%j.out

set -euo pipefail

source ~/mlip4_env.sh
export PYTHONNOUSERSITE=1

cd ~/coursework/new_datasets/water/mtp

mpirun -np 8 python train.py
