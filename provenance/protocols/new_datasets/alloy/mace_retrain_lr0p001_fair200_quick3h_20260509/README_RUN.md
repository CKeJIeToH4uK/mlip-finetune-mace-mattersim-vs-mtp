# MACE alloy fair200 quick retrain lr=0.001

Purpose:
MACE alloy retrain with training budget closer to MatterSim alloy.

MatterSim alloy setup:
- epochs: 200
- early_stop_patience: 50
- train/valid: same alloy split
- model: MatterSim 5M fine-tune

This MACE run:
- max_num_epochs: 200
- patience: 50
- lr: 0.001
- batch_size: 8
- partition: gpu-ef-quick
- time limit: 3h
- no LoRA
- no freeze
- no multihead replay

This is a separate folder. It must not overwrite:
- new_datasets/alloy/mace/
- new_datasets/alloy/mace_retrain_lr0p001_20260508/
- new_datasets/alloy/mace_retrain_lr0p001_quick3h_20260509/

Cluster target path:
/home/brmannanov/coursework/new_datasets/alloy/mace_retrain_lr0p001_fair200_quick3h_20260509

Input files expected on cluster:
- /home/brmannanov/coursework/new_datasets/alloy/convert/train_alloy.xyz
- /home/brmannanov/coursework/new_datasets/alloy/convert/valid_alloy.xyz
- /home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model

Training command:
cd /home/brmannanov/coursework/new_datasets/alloy/mace_retrain_lr0p001_fair200_quick3h_20260509
sbatch train_alloy_mace_lr0p001_fair200_quick3h.sbatch

Eval command after training:
sbatch eval_alloy_mace_lr0p001_fair200_quick3h.sbatch

Expected outputs:
- resources.txt
- exact_command.txt
- train.log
- `alloy_mace_fair200_<jobid>.out`
- `alloy_mace_fair_eval_<jobid>.out`
- eval_valid.json
- eval_train.json
- eval_metrics_fair200_quick3h.csv
- logs/
- results/
- checkpoints/
- models/

Old baseline valid metrics:
- old MACE lr=0.01 Energy MAE = 34.744 meV/atom
- old MACE lr=0.01 Energy RMSE = 64.448 meV/atom
- old MACE lr=0.01 Forces MAE = 70.603 meV/Å
- old MACE lr=0.01 Forces RMSE = 123.247 meV/Å

Acceptance criterion:
- new valid Energy MAE should be below 34.744 meV/atom
- force MAE should be compared explicitly against 70.603 meV/Å

Safe checks before sbatch:
bash -n train_alloy_mace_lr0p001_fair200_quick3h.sbatch
bash -n eval_alloy_mace_lr0p001_fair200_quick3h.sbatch
python -m py_compile eval_mace_alloy.py

Do not run training manually on login node.
