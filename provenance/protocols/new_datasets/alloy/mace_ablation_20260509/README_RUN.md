# MACE alloy normal protocol ablations

Purpose:
Run remaining MACE alloy protocol ablations in the normal partition to avoid gpu-ef-quick preemption.

Experiments:

1. stage2_normal
   - run name: alloy_mace_stage2_normal
   - energy_weight=1
   - forces_weight=100
   - swa enabled
   - start_swa=150
   - swa_lr=0.0003
   - swa_energy_weight=1000
   - swa_forces_weight=100
   - purpose: test whether high energy RMSE is a final-stage convergence problem

2. lora_ew10_normal
   - run name: alloy_mace_lora_ew10_normal
   - energy_weight=10
   - forces_weight=100
   - lora=True
   - lora_rank=4
   - lora_alpha=1.0
   - purpose: test whether full fine-tuning damages the pretrained backbone

3. freeze1_ew10_normal
   - run name: alloy_mace_freeze1_ew10_normal
   - energy_weight=10
   - forces_weight=100
   - freeze=1
   - purpose: test whether preserving the first pretrained layer stabilizes energy predictions

Common:
- lr=0.001
- batch_size=8
- max_num_epochs=200
- patience=50
- eval_interval=25
- loss=weighted
- seed=42
- partition=normal
- one GPU
- same train/valid alloy split
- no multihead replay

Cluster target path:
/home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509

Input files:
- /home/brmannanov/coursework/new_datasets/alloy/convert/train_alloy.xyz
- /home/brmannanov/coursework/new_datasets/alloy/convert/valid_alloy.xyz
- /home/brmannanov/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model

Run:
cd /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509
sbatch train_eval_protocols_normal.sbatch

After job:
python collect_protocols_normal.py
cat protocols_normal_summary.md

Expected outputs:
- run_status_<jobid>.tsv
- stage2_normal/eval_train.json
- stage2_normal/eval_valid.json
- stage2_normal/eval_metrics.csv
- lora_ew10_normal/eval_train.json
- lora_ew10_normal/eval_valid.json
- lora_ew10_normal/eval_metrics.csv
- freeze1_ew10_normal/eval_train.json
- freeze1_ew10_normal/eval_valid.json
- freeze1_ew10_normal/eval_metrics.csv
- protocols_normal_metrics_long.csv
- protocols_normal_summary.md

Interpretation:
Compare to fair200 baseline:
- E MAE 27.523
- E RMSE 86.401
- F MAE 62.076
- F RMSE 113.747

A useful run:
- lowers energy RMSE substantially
- does not make force RMSE much worse

If stage2/LoRA/freeze do not beat EW10/EW50:
- keep them as negative/backup ablations
- main result remains energy-weighted MACE
