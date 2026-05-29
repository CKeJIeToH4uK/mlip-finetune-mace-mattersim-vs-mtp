# MACE alloy retrain lr=0.001

Purpose:
- clean retrain of MACE fine-tune on MoNbTaVW/alloy
- old run had suspiciously weak energy metrics
- main change: lr 0.01 -> 0.001
- old results are not overwritten

Cluster target path:
/home/brmannanov/coursework/new_datasets/alloy/mace_retrain_lr0p001_20260508

Input files expected on cluster:
- /home/brmannanov/coursework/new_datasets/alloy/convert/train_alloy.xyz
- /home/brmannanov/coursework/new_datasets/alloy/convert/valid_alloy.xyz
- /home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model

Run commands on cluster:
cd /home/brmannanov/coursework/new_datasets/alloy/mace_retrain_lr0p001_20260508
bash -n train_alloy_mace_lr0p001.sbatch
bash -n eval_alloy_mace_lr0p001.sbatch
python -m py_compile eval_mace_alloy.py
sbatch train_alloy_mace_lr0p001.sbatch

After training:
sbatch eval_alloy_mace_lr0p001.sbatch

Expected outputs:
- train.log
- resources.txt
- eval_valid.json
- eval_train.json
- alloy_mace_lr0p001_<jobid>.out
- alloy_mace_lr0p001_eval_<jobid>.out
- logs/
- results/
- checkpoints/
- models/

Old baseline:
- valid MAE_E = 34.744 meV/atom
- valid RMSE_E = 64.448 meV/atom
- valid MAE_F = 70.603 meV/A
- valid RMSE_F = 123.247 meV/A

Acceptance criterion:
- new valid MAE_E should be clearly below 34.744 meV/atom
- force MAE should not become much worse than 70.603 meV/A
