# ENSEMBLE AUDIT REPORT 2026-05-11

Scope was limited to the existing `PRESENTATION` materials requested by the task. Slides, TeX files, `main.tex`, training/evaluation runs, raw datasets, checkpoints, model weights, and OCR-derived values were not used as metric sources.

## 1. Directories and archives reviewed

- `PRESENTATION/00_inbox/`
- `PRESENTATION/01_unpacked/`
- `PRESENTATION/03_content/`
- `PRESENTATION/04_assets/`

Archives reviewed in `PRESENTATION/00_inbox/`:

- `presentation_full_context.zip`
- `final_training_bundle_20260510.zip`
- `protocols_eval_addendum_20260510.zip`

## 2. Archives unpacked into staging

- `presentation_full_context.zip` -> `PRESENTATION/01_unpacked/ensemble_audit_20260511/presentation_full_context/`
- `final_training_bundle_20260510.zip` -> `PRESENTATION/01_unpacked/ensemble_audit_20260511/final_training_bundle_20260510_unpacked/`
- `protocols_eval_addendum_20260510.zip` -> `PRESENTATION/01_unpacked/ensemble_audit_20260511/protocols_eval_addendum_20260510_unpacked/`

## 3. Candidate files found

| path | type | dataset | model/protocol/level | split | temperature | metrics present | units | run_id/seed/repeated runs | aggregate mean/std present | accepted/rejected | reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PRESENTATION/00_inbox/final_training_bundle_20260510.zip::final_training_bundle_20260510/sources/alloy/mace_EW10_EW50_normal/full_ew10_normal/eval_train.json | derived/raw metric source | alloy_MoNbTaVW | MACE-EW10 / energy_weight=10 forces_weight=100 normal | train | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | meV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/final_training_bundle_20260510.zip::final_training_bundle_20260510/sources/alloy/mace_EW10_EW50_normal/full_ew10_normal/eval_valid.json | derived/raw metric source | alloy_MoNbTaVW | MACE-EW10 / energy_weight=10 forces_weight=100 normal | valid | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | meV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/final_training_bundle_20260510.zip::final_training_bundle_20260510/sources/alloy/mace_EW10_EW50_normal/full_ew50_normal/eval_train.json | derived/raw metric source | alloy_MoNbTaVW | MACE-EW50 / energy_weight=50 forces_weight=100 normal | train | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | meV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/final_training_bundle_20260510.zip::final_training_bundle_20260510/sources/alloy/mace_EW10_EW50_normal/full_ew50_normal/eval_valid.json | derived/raw metric source | alloy_MoNbTaVW | MACE-EW50 / energy_weight=50 forces_weight=100 normal | valid | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | meV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/final_training_bundle_20260510.zip::final_training_bundle_20260510/sources/alloy/mace_lr1e-3_fair200/eval_train.json | derived/raw metric source | alloy_MoNbTaVW | MACE / lr=0.001 fair200 default loss | train | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | meV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | hyperparameter sweep; indexed but accepted_for_ensemble=false |
| PRESENTATION/00_inbox/final_training_bundle_20260510.zip::final_training_bundle_20260510/sources/alloy/mace_lr1e-3_fair200/eval_valid.json | derived/raw metric source | alloy_MoNbTaVW | MACE / lr=0.001 fair200 default loss | valid | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | meV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | hyperparameter sweep; indexed but accepted_for_ensemble=false |
| PRESENTATION/00_inbox/final_training_bundle_20260510.zip::final_training_bundle_20260510/sources/alloy/mace_lr1e-3_quick250/eval_train.json | derived/raw metric source | alloy_MoNbTaVW | MACE / lr=0.001 quick250 default loss | train | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | meV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | hyperparameter sweep; indexed but accepted_for_ensemble=false |
| PRESENTATION/00_inbox/final_training_bundle_20260510.zip::final_training_bundle_20260510/sources/alloy/mace_lr1e-3_quick250/eval_valid.json | derived/raw metric source | alloy_MoNbTaVW | MACE / lr=0.001 quick250 default loss | valid | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | meV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | hyperparameter sweep; indexed but accepted_for_ensemble=false |
| PRESENTATION/00_inbox/final_training_bundle_20260510.zip::final_training_bundle_20260510/sources/water/mtp_clean20_20260508/metrics_20_clean.json | derived/raw metric source | water_H2O | MTP-20 / level20 clean | train, valid | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | meV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::26.02.26/mtp_errors_summary.csv | derived/raw metric source | organic | MTP-16 / level16, MTP-20 / level20 | train_300K, valid_300K | 300K | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; eV/A | yes | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::26.02.26/sweep_lr_bs_summary.csv | derived/raw metric source | organic | MatterSim / lr=0.0001 batch_size=16, MatterSim / lr=0.0001 batch_size=32, MatterSim / lr=0.0001 batch_size=64, MatterSim / lr=1e-05 batch_size=16, MatterSim / lr=1e-05 batch_size=32, MatterSim / lr=1e-05 batch_size=64, MatterSim / lr=1e-05 batch_size=8, MatterSim / lr=2e-05 batch_size=16, MatterSim / lr=2e-05 batch_size=32, MatterSim / lr=2e-05 batch_size=64, MatterSim / lr=2e-05 batch_size=8, MatterSim / lr=5e-05 batch_size=16, MatterSim / lr=5e-05 batch_size=32, MatterSim / lr=5e-05 batch_size=64, MatterSim / lr=5e-05 batch_size=8 | valid_300K | 300K | none standardized | ambiguous in CSV | run/seed indicated in filename/path for some rows | no | rejected | hyperparameter sweep; indexed but accepted_for_ensemble=false |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mace/test_1200K.json | derived/raw metric source | organic | MACE / fine-tuned organic 300K | test_1200K | 1200K | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | no | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mace/test_300K.json | derived/raw metric source | organic | MACE / fine-tuned organic 300K | test_300K | 300K | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | no | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mace/test_600K.json | derived/raw metric source | organic | MACE / fine-tuned organic 300K | test_600K | 600K | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | no | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mattersim/test_1200K.json | derived/raw metric source | organic | MatterSim / fine-tuned organic 300K | test_1200K | 1200K | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | no | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mattersim/test_300K.json | derived/raw metric source | organic | MatterSim / fine-tuned organic 300K | test_300K | 300K | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | no | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mattersim/test_600K.json | derived/raw metric source | organic | MatterSim / fine-tuned organic 300K | test_600K | 600K | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | no | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mtp/test_1200K_mtp16.json | derived/raw metric source | organic | MTP-16 / level16 | test_1200K | 1200K | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mtp/test_1200K_mtp20.json | derived/raw metric source | organic | MTP-20 / level20 | test_1200K | 1200K | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mtp/test_300K_mtp16.json | derived/raw metric source | organic | MTP-16 / level16 | test_300K | 300K | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mtp/test_300K_mtp20.json | derived/raw metric source | organic | MTP-20 / level20 | test_300K | 300K | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mtp/test_600K_mtp16.json | derived/raw metric source | organic | MTP-16 / level16 | test_600K | 600K | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mtp/test_600K_mtp20.json | derived/raw metric source | organic | MTP-20 / level20 | test_600K | 600K | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/alloy/mace/eval_train.json | derived/raw metric source | alloy_MoNbTaVW | MACE / default old lr=0.01 | train | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | no | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/alloy/mace/eval_valid.json | derived/raw metric source | alloy_MoNbTaVW | MACE / default old lr=0.01 | valid | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | no | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/alloy/mattersim/eval_train.json | derived/raw metric source | alloy_MoNbTaVW | MatterSim / fine-tuned reference | train | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | no | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/alloy/mattersim/eval_valid.json | derived/raw metric source | alloy_MoNbTaVW | MatterSim / fine-tuned reference | valid | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | no | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/alloy/mtp/metrics.json | derived/raw metric source | alloy_MoNbTaVW | MTP-16 / level16 | train, valid | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; eV/A | no | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/alloy/mtp/metrics_20.json | derived/raw metric source | alloy_MoNbTaVW | MTP-20 / level20 | train, valid | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; eV/A | no | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/water/mace/eval_train.json | derived/raw metric source | water_H2O | MACE / fine-tuned | train | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | no | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/water/mace/eval_valid.json | derived/raw metric source | water_H2O | MACE / fine-tuned | valid | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | no | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/water/mattersim/eval_train.json | derived/raw metric source | water_H2O | MatterSim / fine-tuned | train | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | no | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/water/mattersim/eval_valid.json | derived/raw metric source | water_H2O | MatterSim / fine-tuned | valid | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; meV/A | no | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/water/mtp/metrics.json | derived/raw metric source | water_H2O | MTP-16 / level16 (old folder mislabeled mtp20) | train, valid | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | eV/atom; eV/A | no | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/protocols_eval_addendum_20260510.zip::protocols_eval_addendum_20260510/sources/mace_ablation_normal_protocols_20260509/freeze1_ew10_normal/eval_train.json | derived/raw metric source | alloy_MoNbTaVW | MACE-freeze1-EW10 / partial freeze=1, energy_weight=10 forces_weight=100 | train | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | meV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/protocols_eval_addendum_20260510.zip::protocols_eval_addendum_20260510/sources/mace_ablation_normal_protocols_20260509/freeze1_ew10_normal/eval_valid.json | derived/raw metric source | alloy_MoNbTaVW | MACE-freeze1-EW10 / partial freeze=1, energy_weight=10 forces_weight=100 | valid | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | meV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/protocols_eval_addendum_20260510.zip::protocols_eval_addendum_20260510/sources/mace_ablation_normal_protocols_20260509/lora_ew10_normal/eval_train.json | derived/raw metric source | alloy_MoNbTaVW | MACE-LoRA-EW10 / LoRA, energy_weight=10 forces_weight=100 | train | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | meV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/protocols_eval_addendum_20260510.zip::protocols_eval_addendum_20260510/sources/mace_ablation_normal_protocols_20260509/lora_ew10_normal/eval_valid.json | derived/raw metric source | alloy_MoNbTaVW | MACE-LoRA-EW10 / LoRA, energy_weight=10 forces_weight=100 | valid | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | meV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/protocols_eval_addendum_20260510.zip::protocols_eval_addendum_20260510/sources/mace_ablation_normal_protocols_20260509/stage2_normal/eval_train.json | derived/raw metric source | alloy_MoNbTaVW | MACE-stage2 / stage-two/SWA energy convergence | train | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | meV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/protocols_eval_addendum_20260510.zip::protocols_eval_addendum_20260510/sources/mace_ablation_normal_protocols_20260509/stage2_normal/eval_valid.json | derived/raw metric source | alloy_MoNbTaVW | MACE-stage2 / stage-two/SWA energy convergence | valid | NA | energy MAE, energy RMSE, forces MAE, forces RMSE | meV/atom; meV/A | run/seed indicated in filename/path for some rows | no | accepted | standardized into raw run index |
| PRESENTATION/00_inbox/presentation_full_context.zip::19.03.26/cross_temp_eval_300_600_1200K_current/results/* | duplicate result snapshot | mixed | mixed | mixed | mixed | same metrics as canonical repo copy | same as canonical | no new runs | no | rejected | SHA-identical dated duplicate; not counted as repeated run |
| PRESENTATION/00_inbox/presentation_full_context.zip::19.03.26/initial_eval/results/* | duplicate result snapshot | mixed | mixed | mixed | mixed | same metrics as canonical repo copy | same as canonical | no new runs | no | rejected | SHA-identical dated duplicate; not counted as repeated run |
| PRESENTATION/00_inbox/presentation_full_context.zip::26.02.26/sweep_lr_bs_history.csv | curve/sweep CSV | organic | MatterSim | train/valid 300K | 300K | per-epoch loss/MAE columns, not final standardized run metrics | units not explicit in CSV | multiple hyperparameter rows for sweep or one curve | no | rejected for ensemble | learning/sweep evidence only; not a repeated same-protocol ensemble |
| PRESENTATION/00_inbox/presentation_full_context.zip::26.02.26/epoch_vs_err_curve.csv | curve/sweep CSV | organic | MatterSim | train/valid 300K | 300K | per-epoch loss/MAE columns, not final standardized run metrics | units not explicit in CSV | multiple hyperparameter rows for sweep or one curve | no | rejected for ensemble | learning/sweep evidence only; not a repeated same-protocol ensemble |
| PRESENTATION/00_inbox/presentation_full_context.zip::26.02.26/mace_finetune/ft_300K/results/ft_300K_run-42_train.txt | JSONL learning curve | organic | MACE run-42 | validation curve | 300K | per-epoch validation loss/MAE/RMSE | metric keys clear, curve only | single run-42 | no | accepted for curve provenance, rejected for ensemble | not repeated curves; no mean/std band |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/water/mace/results/water_ft_run-42_train.txt | JSONL learning curve | water_H2O | MACE run-42 | validation curve | NA | per-epoch validation loss/MAE/RMSE | metric keys clear, curve only | single run-42 | no | accepted for curve provenance, rejected for ensemble | not repeated curves; no mean/std band |
| PRESENTATION/04_assets/figures/**/*.{png,pdf} | figure assets | mixed | mixed | mixed | mixed | visuals only | not used | not applicable | no | rejected as numeric source | 26 figure files present; OCR/image-derived numbers are prohibited by task |
| PRESENTATION/00_inbox/presentation_full_context.zip | archive | mixed | mixed | mixed | mixed | archive container | mixed | not a metric row | no | accepted for discovery | unpacked into staging and only text/table/log files used |
| PRESENTATION/00_inbox/final_training_bundle_20260510.zip | archive | mixed | mixed | mixed | mixed | archive container | mixed | not a metric row | no | accepted for discovery | unpacked into staging and only text/table/log files used |
| PRESENTATION/00_inbox/protocols_eval_addendum_20260510.zip | archive | mixed | mixed | mixed | mixed | archive container | mixed | not a metric row | no | accepted for discovery | unpacked into staging and only text/table/log files used |

## 4. Files rejected and why

| path | type | dataset | model/protocol/level | accepted/rejected | reason |
| --- | --- | --- | --- | --- | --- |
| PRESENTATION/00_inbox/presentation_full_context.zip::26.02.26/sweep_lr_bs_summary.csv | derived/raw metric source | organic | MatterSim / lr=0.0001 batch_size=16, MatterSim / lr=0.0001 batch_size=32, MatterSim / lr=0.0001 batch_size=64, MatterSim / lr=1e-05 batch_size=16, MatterSim / lr=1e-05 batch_size=32, MatterSim / lr=1e-05 batch_size=64, MatterSim / lr=1e-05 batch_size=8, MatterSim / lr=2e-05 batch_size=16, MatterSim / lr=2e-05 batch_size=32, MatterSim / lr=2e-05 batch_size=64, MatterSim / lr=2e-05 batch_size=8, MatterSim / lr=5e-05 batch_size=16, MatterSim / lr=5e-05 batch_size=32, MatterSim / lr=5e-05 batch_size=64, MatterSim / lr=5e-05 batch_size=8 | rejected | hyperparameter sweep; indexed but accepted_for_ensemble=false |
| PRESENTATION/00_inbox/presentation_full_context.zip::19.03.26/cross_temp_eval_300_600_1200K_current/results/* | duplicate result snapshot | mixed | mixed | rejected | SHA-identical dated duplicate; not counted as repeated run |
| PRESENTATION/00_inbox/presentation_full_context.zip::19.03.26/initial_eval/results/* | duplicate result snapshot | mixed | mixed | rejected | SHA-identical dated duplicate; not counted as repeated run |
| PRESENTATION/00_inbox/presentation_full_context.zip::26.02.26/sweep_lr_bs_history.csv | curve/sweep CSV | organic | MatterSim | rejected for ensemble | learning/sweep evidence only; not a repeated same-protocol ensemble |
| PRESENTATION/00_inbox/presentation_full_context.zip::26.02.26/epoch_vs_err_curve.csv | curve/sweep CSV | organic | MatterSim | rejected for ensemble | learning/sweep evidence only; not a repeated same-protocol ensemble |
| PRESENTATION/00_inbox/presentation_full_context.zip::26.02.26/mace_finetune/ft_300K/results/ft_300K_run-42_train.txt | JSONL learning curve | organic | MACE run-42 | accepted for curve provenance, rejected for ensemble | not repeated curves; no mean/std band |
| PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/water/mace/results/water_ft_run-42_train.txt | JSONL learning curve | water_H2O | MACE run-42 | accepted for curve provenance, rejected for ensemble | not repeated curves; no mean/std band |
| PRESENTATION/04_assets/figures/**/*.{png,pdf} | figure assets | mixed | mixed | rejected as numeric source | 26 figure files present; OCR/image-derived numbers are prohibited by task |

## 5. Run type classification

| dataset | model/protocol/level | run_type | rows |
| --- | --- | --- | --- |
| alloy_MoNbTaVW | MACE / default old lr=0.01 | protocol_ablation | 2 |
| alloy_MoNbTaVW | MACE / lr=0.001 fair200 default loss | hyperparameter_sweep | 2 |
| alloy_MoNbTaVW | MACE / lr=0.001 quick250 default loss | hyperparameter_sweep | 2 |
| alloy_MoNbTaVW | MACE-EW10 / energy_weight=10 forces_weight=100 normal | protocol_ablation | 2 |
| alloy_MoNbTaVW | MACE-EW50 / energy_weight=50 forces_weight=100 normal | protocol_ablation | 2 |
| alloy_MoNbTaVW | MACE-LoRA-EW10 / LoRA, energy_weight=10 forces_weight=100 | protocol_ablation | 2 |
| alloy_MoNbTaVW | MACE-freeze1-EW10 / partial freeze=1, energy_weight=10 forces_weight=100 | protocol_ablation | 2 |
| alloy_MoNbTaVW | MACE-stage2 / stage-two/SWA energy convergence | protocol_ablation | 2 |
| alloy_MoNbTaVW | MTP-16 / level16 | single_run | 2 |
| alloy_MoNbTaVW | MTP-20 / level20 | single_run | 2 |
| alloy_MoNbTaVW | MatterSim / fine-tuned reference | single_run | 2 |
| organic | MACE / fine-tuned organic 300K | single_run | 3 |
| organic | MTP-16 / level16 | single_run | 3 |
| organic | MTP-16 / level16 | true_ensemble_or_repeated_runs | 10 |
| organic | MTP-20 / level20 | single_run | 3 |
| organic | MTP-20 / level20 | true_ensemble_or_repeated_runs | 10 |
| organic | MatterSim / fine-tuned organic 300K | single_run | 3 |
| organic | MatterSim / lr=0.0001 batch_size=16 | hyperparameter_sweep | 1 |
| organic | MatterSim / lr=0.0001 batch_size=32 | hyperparameter_sweep | 1 |
| organic | MatterSim / lr=0.0001 batch_size=64 | hyperparameter_sweep | 1 |
| organic | MatterSim / lr=1e-05 batch_size=16 | hyperparameter_sweep | 1 |
| organic | MatterSim / lr=1e-05 batch_size=32 | hyperparameter_sweep | 1 |
| organic | MatterSim / lr=1e-05 batch_size=64 | hyperparameter_sweep | 1 |
| organic | MatterSim / lr=1e-05 batch_size=8 | hyperparameter_sweep | 1 |
| organic | MatterSim / lr=2e-05 batch_size=16 | hyperparameter_sweep | 1 |
| organic | MatterSim / lr=2e-05 batch_size=32 | hyperparameter_sweep | 1 |
| organic | MatterSim / lr=2e-05 batch_size=64 | hyperparameter_sweep | 1 |
| organic | MatterSim / lr=2e-05 batch_size=8 | hyperparameter_sweep | 1 |
| organic | MatterSim / lr=5e-05 batch_size=16 | hyperparameter_sweep | 1 |
| organic | MatterSim / lr=5e-05 batch_size=32 | hyperparameter_sweep | 1 |
| organic | MatterSim / lr=5e-05 batch_size=64 | hyperparameter_sweep | 1 |
| organic | MatterSim / lr=5e-05 batch_size=8 | hyperparameter_sweep | 1 |
| water_H2O | MACE / fine-tuned | single_run | 2 |
| water_H2O | MTP-16 / level16 (old folder mislabeled mtp20) | single_run | 2 |
| water_H2O | MTP-20 / level20 clean | single_run | 2 |
| water_H2O | MatterSim / fine-tuned | single_run | 2 |

Classification definitions used:

- `single_run`: one model/protocol run for the exact dataset/split/temperature/metric.
- `true_ensemble_or_repeated_runs`: repeated MTP job IDs within the same organic MTP level and train/valid 300K split.
- `protocol_ablation`: MACE default/EW/LoRA/freeze/stage2 style protocol changes; never aggregated as ensemble.
- `hyperparameter_sweep`: lr/batch/budget choices; never aggregated as ensemble.
- `ambiguous`: not used here for accepted aggregates; ambiguous unit rows are marked non-ensemble.

## 6. Ensemble eligibility findings

- Organic cross-temperature `test_300K`, `test_600K`, and `test_1200K`: all MatterSim, MACE, MTP-16, and MTP-20 rows are `single_run`; no mean ± std is supported for those plots.
- Organic MTP train/valid 300K: five repeated job IDs exist for MTP-16 and five for MTP-20 in `26.02.26/mtp_errors_summary.csv`; these are the only rows accepted for mean ± std.
- H2O/water: MatterSim, MACE, MTP-16, and clean MTP-20 are single runs; no ensemble evidence.
- MoNbTaVW/alloy: MatterSim and MTP-20 are single runs. MACE default, EW10, EW50, LoRA, freeze, and stage2 are protocol ablations/sweeps, not ensembles.
- Learning curves: no repeated curves were found for MatterSim or MACE; curves should remain representative single-run curves without bands.

## 7. Generated CSV inventory

- `PRESENTATION/03_content/ensemble_raw_runs_index_20260511.csv`
- `PRESENTATION/03_content/ensemble_coverage_matrix_20260511.csv`
- `PRESENTATION/03_content/ensemble_aggregates_verified_20260511.csv`

## Final decision for slides

| dataset | model/protocol | split/temp | status | slide action |
| --- | --- | --- | --- | --- |
| organic | MatterSim | test_300K/test_600K/test_1200K | single run: show line/bar only | Show a single run; do not add std to cross-temperature plots |
| organic | MACE | test_300K/test_600K/test_1200K | single run: show line/bar only | Show a single run; do not add std to cross-temperature plots |
| organic | MTP-16 | test_300K/test_600K/test_1200K | single run: show line/bar only | Show a single run; do not add std to cross-temperature plots |
| organic | MTP-20 | test_300K/test_600K/test_1200K | single run: show line/bar only | Show a single run; do not add std to cross-temperature plots |
| organic | MTP-16 | train_300K and valid_300K | ensemble: show mean ± std | Show mean ± std only in train/valid MTP baseline/backup table, not cross-temp test plot |
| organic | MTP-20 | train_300K and valid_300K | ensemble: show mean ± std | Show mean ± std only in train/valid MTP baseline/backup table, not cross-temp test plot |
| organic | MatterSim sweep | valid_300K | ablation/sweep: no std | Do not aggregate; hyperparameter sweep |
| water_H2O | MatterSim | train/valid where available | single run: show line/bar only | Show a single run; no mean ± std |
| water_H2O | MACE | train/valid where available | single run: show line/bar only | Show a single run; no mean ± std |
| water_H2O | MTP-16 | train/valid where available | single run: show line/bar only | Show a single run; no mean ± std |
| water_H2O | MTP-20 | train/valid where available | single run: show line/bar only | Show a single run; no mean ± std |
| alloy_MoNbTaVW | MatterSim | train/valid where available | single run: show line/bar only | Show a single run |
| alloy_MoNbTaVW | MACE default | train/valid where available | ablation: show separate protocol row, no std | Do not aggregate; ablation/sweep |
| alloy_MoNbTaVW | MACE-EW10 | train/valid where available | ablation: show separate protocol row, no std | Do not aggregate; ablation/sweep |
| alloy_MoNbTaVW | MACE-EW50 | train/valid where available | ablation: show separate protocol row, no std | Do not aggregate; ablation/sweep |
| alloy_MoNbTaVW | MACE LoRA/freeze/stage2 | train/valid where available | ablation: show separate protocol row, no std | Do not aggregate; ablation/sweep |
| alloy_MoNbTaVW | MTP-20 | train/valid where available | single run: show line/bar only | Show a single run; no mean ± std |

Current slides to revise:

1. Any organic cross-temperature plot that currently shows ensemble mean ± std for MatterSim, MACE, MTP-16, or MTP-20 should be revised to single-run lines/bars.
2. Any MoNbTaVW plot that treats MACE default/EW10/EW50/LoRA/freeze/stage2 as an ensemble should be revised to separate protocol rows without std.
3. Any H2O bar plot with std/error bars should be revised to single-run bars unless a future repeated-run source is added.

Slides not to touch based on this audit:

1. Learning-curve slides that show representative single-run curves without bands.
2. Cross-temperature organic slides if they already show one line/bar per model without std.
3. H2O and MoNbTaVW slides if they already show single-run or separate protocol rows without std.

Backup slides to update:

1. MTP baseline/backup table may show mean ± std only for organic MTP-16/MTP-20 train_300K and valid_300K repeated job IDs.
2. Protocol-ablation backup should label MACE-EW10, MACE-EW50, LoRA, freeze, and stage2 as ablations, not ensemble members.

Verification notes:

- Numeric aggregate rows were computed only from `accepted_for_ensemble=true`.
- No aggregate mixes MACE default with EW10/EW50, MTP-16 with MTP-20, train with valid/test, or organic temperatures.
- Source rows with ambiguous units were left out of ensemble aggregation.
