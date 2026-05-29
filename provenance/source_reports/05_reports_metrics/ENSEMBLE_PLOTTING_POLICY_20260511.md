# ENSEMBLE PLOTTING POLICY 2026-05-11

## Organic

- MatterSim test_300K/test_600K/test_1200K: SHOW single run.
- MACE test_300K/test_600K/test_1200K: SHOW single run.
- MTP-16 test_300K/test_600K/test_1200K: SHOW single run.
- MTP-20 test_300K/test_600K/test_1200K: SHOW single run.
- MTP-16 train_300K and valid_300K repeated job IDs: SHOW mean ± std, but only in a train/validation MTP baseline or backup table.
- MTP-20 train_300K and valid_300K repeated job IDs: SHOW mean ± std, but only in a train/validation MTP baseline or backup table.
- MatterSim lr/batch variants: DO NOT aggregate: ablation/sweep.
- Current cross-temperature plots should not get ensemble bands/error bars. Caption language: `Points/lines are single evaluated model artifacts; no std is shown because repeated runs were not available for the same model, split, temperature, and metric.`

## H2O

- MatterSim train/valid: SHOW single run.
- MACE train/valid: SHOW single run.
- MTP-16 train/valid: SHOW single run.
- MTP-20 clean train/valid: SHOW single run.
- No H2O ensemble evidence was found. Recommended plot: single-run bars without std. Caption language: `Bars are single-run validation metrics; no repeated seeds were available in the presentation materials.`

## MoNbTaVW

- MatterSim train/valid: SHOW single run.
- MTP-20 train/valid: SHOW single run.
- MACE default old lr=0.01: DO NOT aggregate: ablation/sweep; show as its own protocol row if used.
- MACE-EW10: DO NOT aggregate: ablation/sweep; show as its own protocol row.
- MACE-EW50: DO NOT aggregate: ablation/sweep; show as its own protocol row.
- LoRA / freeze / stage2: DO NOT aggregate: ablation/sweep; keep in backup/ablation context, no std.
- MACE-EW10 and MACE-EW50 are protocol variants, not ensemble members of default MACE. Recommended caption language: `MACE rows are protocol ablations with different loss/fine-tuning settings; they are shown separately and are not averaged.`

## Learning curves

- Organic MatterSim and MACE curves: SHOW single run / representative curve.
- H2O MatterSim and MACE curves: SHOW single run / representative curve.
- MTP raw optimizer traces: INSUFFICIENT evidence for clean validation-curve bands.
- Do not show bands: no repeated curves were found for the same dataset + model/protocol + split + metric.

## General rule

SHOW mean ± std only when all grouping keys match exactly: dataset + model/protocol/level + split + temperature + metric, and there are repeated run IDs/seeds. Otherwise use SHOW single run, DO NOT aggregate: ablation/sweep, or INSUFFICIENT evidence.
