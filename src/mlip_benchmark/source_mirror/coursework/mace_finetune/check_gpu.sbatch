#!/bin/bash
#SBATCH -A proj_1786
#SBATCH --job-name=mace_smoke
#SBATCH --output=mace/mace_smoke-%j.log
#SBATCH --error=mace/mace_smoke-%j.err
#SBATCH --time=0:15:00
#SBATCH --gpus=1
#SBATCH --cpus-per-task=1

cd "$SLURM_SUBMIT_DIR"

source ~/.bashrc
conda activate mace

mace_run_train \
  --name smoke_300K_pbc \
  --device cuda \
  --train_file databases/train_300K.xyz \
  --test_file databases/test_300K.xyz \
  --valid_fraction 0.1 \
  --energy_key energy \
  --forces_key forces \
  --atomic_numbers "[1, 6, 7, 8]" \
  --r_max 5.0 \
  --batch_size 4 \
  --max_num_epochs 5 \
  --eval_interval 1 \
  --num_workers 0 \
  --multiheads_finetuning=False \
  --E0s=average