# MACE alloy EW10/EW50 normal runs

Purpose:
Run EW10 and EW50 MACE alloy experiments in normal partition to avoid gpu-ef-quick preemption.

Background:
- Default/fair200 MACE had high energy RMSE.
- EW10 quick partial run reached approximately:
  RMSE_E = 29 meV/atom
  RMSE_F = 115 meV/Å
  before preemption.
- Therefore EW10/EW50 are the most important MACE ablations.

Runs:
1. full_ew10_normal:
   energy_weight=10
   forces_weight=100
2. full_ew50_normal:
   energy_weight=50
   forces_weight=100

Common:
- lr=0.001
- batch_size=8
- max_num_epochs=200
- patience=50
- loss=weighted
- seed=42
- partition=normal
- one GPU
- same train/valid split

Cluster target path:
/home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509

Run:
cd /home/brmannanov/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509
sbatch train_eval_ew10_ew50_normal.sbatch

After job:
python collect_ew10_ew50_normal.py
cat ew10_ew50_normal_summary.md

Expected outputs:
- full_ew10_normal/eval_train.json
- full_ew10_normal/eval_valid.json
- full_ew10_normal/eval_metrics.csv
- full_ew50_normal/eval_train.json
- full_ew50_normal/eval_valid.json
- full_ew50_normal/eval_metrics.csv
- ew10_ew50_normal_metrics_long.csv
- ew10_ew50_normal_summary.md

Interpretation:
Compare with fair200 baseline:
E MAE = 27.523 meV/atom
E RMSE = 86.401 meV/atom
F MAE = 62.076 meV/Å
F RMSE = 113.747 meV/Å

A useful result:
- substantially lower energy RMSE
- forces not much worse
