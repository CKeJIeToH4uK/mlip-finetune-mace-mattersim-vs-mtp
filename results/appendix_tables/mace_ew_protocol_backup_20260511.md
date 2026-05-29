# MACE Energy-Weighted Protocol Backup, 2026-05-11

## Local protocol meanings

- `MACE default` locally refers to the MoNbTaVW fair comparison baseline with `lr=0.001`, `fair200`, and default loss, as listed in `monbtavw_metrics_verified_20260511.csv` and `results_handoff/alloy_mace_ablation_table.md`.
- `MACE-EW10` refers to the completed energy-weighted MACE protocol with `energy_weight=10` and `forces_weight=100` in the normal alloy ablation run.
- `MACE-EW50` refers to the completed energy-weighted MACE protocol with `energy_weight=50` and `forces_weight=100` in the normal alloy ablation run.

MACE-EW50 != default MACE

## Why EW50 appears in main results

EW50 appears in the main MoNbTaVW result because project handoff materials identify it as the best completed MACE energy result among the completed MACE alloy runs. The final caveat is that it must be labeled as `MACE-EW50` or energy-weighted MACE, not as default MACE.

## Verified weights

The EW10 and EW50 loss weights are explicitly verified in project materials: `energy_weight=10 forces_weight=100 normal` for EW10 and `energy_weight=50 forces_weight=100 normal` for EW50. The architecture slide `arch_18_mace_finetuning_loss_weights.tex` also shows local default weights as `w_E=1`, `w_F=100`; the source reports describe that row as `default loss`.

## Caveat

The MACE rows are protocol ablations with different loss/fine-tuning settings. They are shown separately and are not averaged as an ensemble.
