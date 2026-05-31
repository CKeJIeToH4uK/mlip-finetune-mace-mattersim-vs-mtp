#!/bin/bash
#SBATCH --job-name=ms_eval
#SBATCH --gpus=1
#SBATCH --cpus-per-task=4
#SBATCH --time=02:00:00
#SBATCH -A proj_1786
#SBATCH --output=~/coursework/mattersim_finetune/1-5million/5m/best_err/slurm-%j.out

set -euo pipefail

# 1) окружение (вариант A: твой env-скрипт, который ты уже юзал)
source ~/mlip4_env.sh
# или вариант B: conda (если у тебя так принято)
# source ~/miniconda3/etc/profile.d/conda.sh
# conda activate mlip-4

# 2) на всякий
cd ~/coursework

# 3) запуск
srun python ~/coursework/test_finetune_mattersim.py