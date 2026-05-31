# MACE alloy retrain quick3h lr=0.001

Purpose:
Quick parallel retrain of MACE on MoNbTaVW/alloy using gpu-ef-quick.

This is a separate run folder. It must not overwrite:
- old baseline folder: new_datasets/alloy/mace/
- normal retrain folder: new_datasets/alloy/mace_retrain_lr0p001_20260508/

Why:
The normal retrain is pending in normal partition.
Old MACE alloy metrics had substantially higher energy errors than the target comparison rows.
The main hypothesis is that old lr=0.01 was too high.
This quick run tests lr=0.001 with a 3-hour partition limit.

Cluster target path:
/home/brmannanov/coursework/new_datasets/alloy/mace_retrain_lr0p001_quick3h_20260509

Input files expected on cluster:
- /home/brmannanov/coursework/new_datasets/alloy/convert/train_alloy.xyz
- /home/brmannanov/coursework/new_datasets/alloy/convert/valid_alloy.xyz
- /home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model

Training command:
cd /home/brmannanov/coursework/new_datasets/alloy/mace_retrain_lr0p001_quick3h_20260509
sbatch train_alloy_mace_lr0p001_quick3h.sbatch

Eval command after training:
sbatch eval_alloy_mace_lr0p001_quick3h.sbatch

Training setup:
- partition: gpu-ef-quick
- time limit: 3h
- lr: 0.001
- max_num_epochs: 250
- patience: 75
- batch_size: 8
- seed: 42
- foundation model: /home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model
- no LoRA
- no freeze
- no multihead replay

Expected outputs:
- resources.txt
- exact_command.txt
- train.log
- `alloy_mace_q3h_<jobid>.out`
- `alloy_mace_q3h_eval_<jobid>.out`
- eval_valid.json
- eval_train.json
- eval_metrics_quick3h.csv
- logs/
- results/
- checkpoints/
- models/

Old baseline valid metrics:
- Energy MAE = 34.744 meV/atom
- Energy RMSE = 64.448 meV/atom
- Forces MAE = 70.603 meV/Å
- Forces RMSE = 123.247 meV/Å

Acceptance criterion:
- new valid Energy MAE should be below 34.744 meV/atom
- force MAE should be compared explicitly against 70.603 meV/Å

Safe checks before sbatch:
bash -n train_alloy_mace_lr0p001_quick3h.sbatch
bash -n eval_alloy_mace_lr0p001_quick3h.sbatch
python -m py_compile eval_mace_alloy.py

Do not run training manually on login node.
