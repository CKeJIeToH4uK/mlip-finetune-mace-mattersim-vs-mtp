# ENSEMBLE PLOTTING POLICY 2026-05-11

## Organic

- MatterSim test_300K/test_600K/test_1200K: show a single run.
- MACE test_300K/test_600K/test_1200K: show a single run.
- MTP-16 test_300K/test_600K/test_1200K: show a single run.
- MTP-20 test_300K/test_600K/test_1200K: show a single run.
- MTP-16 train_300K and valid_300K repeated job IDs: show mean ± std, but only in a train/validation MTP baseline or backup table.
- MTP-20 train_300K and valid_300K repeated job IDs: show mean ± std, but only in a train/validation MTP baseline or backup table.
- MatterSim lr/batch variants: do not aggregate; treat as ablation/sweep rows.
- Current cross-temperature plots should not get ensemble bands/error bars. Caption language: `Points/lines are single evaluated model artifacts; no std is shown because repeated runs were not available for the same model, split, temperature, and metric.`

## H2O

- MatterSim train/valid: show a single run.
- MACE train/valid: show a single run.
- MTP-16 train/valid: show a single run.
- MTP-20 clean train/valid: show a single run.
- No H2O ensemble evidence was found. Recommended plot: single-run bars without std. Caption language: `Bars are single-run validation metrics; no repeated seeds were available in the presentation materials.`

## MoNbTaVW

- MatterSim train/valid: show a single run.
- MTP-20 train/valid: show a single run.
- MACE default old lr=0.01: do not aggregate; show as its own protocol row if used.
- MACE-EW10: do not aggregate; show as its own protocol row.
- MACE-EW50: do not aggregate; show as its own protocol row.
- LoRA / freeze / stage2: do not aggregate; keep in backup/ablation context, no std.
- MACE-EW10 and MACE-EW50 are protocol variants, not ensemble members of default MACE. Recommended caption language: `MACE rows are protocol ablations with different loss/fine-tuning settings; they are shown separately and are not averaged.`

## Learning curves

- Organic MatterSim and MACE curves: show a single run / representative curve.
- H2O MatterSim and MACE curves: show a single run / representative curve.
- MTP raw optimizer traces: insufficient evidence for clean validation-curve bands.
- Do not show bands: no repeated curves were found for the same dataset + model/protocol + split + metric.

## General rule

Show mean ± std only when all grouping keys match exactly: dataset, model/protocol/level, split, temperature, and metric, and when repeated run IDs/seeds are available. In all other cases, use a single-run visualization and do not aggregate ablations or sweeps.
