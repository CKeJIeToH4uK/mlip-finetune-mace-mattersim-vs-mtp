# H2O DATA DISCOVERY REPORT 2026-05-11

## 1. Directories/archives searched

- `PRESENTATION/03_content/results_handoff/`
- `PRESENTATION/03_content/`
- `PRESENTATION/04_assets/`
- `PRESENTATION/00_inbox/presentation_full_context.zip`
- `PRESENTATION/00_inbox/final_training_bundle_20260510.zip`
- `PRESENTATION/00_inbox/protocols_eval_addendum_20260510.zip` (searched by inventory; no accepted H2O metric rows needed from it)
- staging extraction: `PRESENTATION/01_unpacked/h2o_discovery_20260511/`

Only source/metric materials needed for the deck were copied. Raw datasets, checkpoints, and model weights were not copied into deck/assets.

## 2. Candidate files found

| path | type | models present | split present | metrics present | units | decision | reason |
|---|---|---|---|---|---|---|---|
| `FINAL_NEW_CHAT_CONTEXT_20260511/05_reports_metrics/results_handoff/final_metrics_wide.csv` | CSV | MTP-16, MTP-20 | valid; MTP-20 train | Energy MAE/RMSE, Forces MAE/RMSE | meV/atom; meV/Å | accepted for MTP rows | final verified H2O MTP source |
| `FINAL_NEW_CHAT_CONTEXT_20260511/05_reports_metrics/results_handoff/final_metrics_long.csv` | CSV | MTP-16, MTP-20 | valid; MTP-20 train | Energy MAE/RMSE, Forces MAE/RMSE | meV/atom; meV/Å | accepted for cross-check | final verified H2O MTP source |
| `PRESENTATION/03_content/results_handoff/water_mtp_table.md` | Markdown | MTP-16, MTP-20 | valid; MTP-20 train | Energy MAE/RMSE, Forces MAE/RMSE | implied final table units | accepted for cross-check | MTP anchor table |
| `PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/water/mattersim/eval_valid.json` | JSON | MatterSim | water_valid | Energy MAE/RMSE, Forces MAE/RMSE | eV/atom; eV/A; force meV/A also present | accepted | H2O validation eval JSON with clear units |
| `PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/water/mace/eval_valid.json` | JSON | MACE | water_valid | Energy MAE/RMSE, Forces MAE/RMSE | eV/atom; eV/A; force meV/A also present | accepted | H2O validation eval JSON with clear units |
| `PRESENTATION/00_inbox/presentation_full_context.zip::for_gpt/metrics/05_new_datasets_metrics_long.csv` | CSV | MatterSim, MACE, old MTP | train/valid | Energy MAE/RMSE, Forces MAE/RMSE | eV/atom; eV/A; meV/A for forces | accepted as corroborating source | values match accepted eval JSON; not used for final MTP rows |
| `PRESENTATION/00_inbox/presentation_full_context.zip::for_gpt/metrics/05_new_datasets_summary.md` | Markdown | MatterSim, MACE, old MTP | train/valid | Energy MAE/RMSE, Forces MAE/RMSE | eV/atom; eV/A | accepted as corroborating source | documents schema and warns about old water MTP naming |
| `PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/figures/water_mae.png` | PNG | MatterSim, MACE, old MTP | train/valid | plotted MAE only | image only | rejected as numeric source | image was used only as discovery clue; no OCR |
| `PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/figures/water_rmse.png` | PNG | MatterSim, MACE, old MTP | train/valid | plotted RMSE only | image only | rejected as numeric source | image was used only as discovery clue; no OCR |
| `PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/analysis_v2.ipynb` | notebook | MatterSim, MACE, old MTP | train/valid | plotting code reads eval JSON/MTP metrics | source-dependent | accepted for provenance only | notebook was inspected, not executed |
| `PRESENTATION/00_inbox/final_training_bundle_20260510.zip::final_training_bundle_20260510/sources/water/mtp_clean20_20260508/metrics_20_clean.json` | JSON | MTP-20 | train/valid | Energy MAE/RMSE, Forces MAE/RMSE | meV/atom; meV/Å | accepted for cross-check | agrees with final metrics table |
| `PRESENTATION/00_inbox/final_training_bundle_20260510.zip::final_training_bundle_20260510/sources/water/mtp_old_level16/metrics.json` | JSON | MTP-16 | train/valid | Energy MAE/RMSE, Forces MAE/RMSE in raw error strings | eV/atom; eV/A | accepted for cross-check | agrees with final metrics table; final table remains source for MTP rows |

## 3. Final canonical H2O table

All values below are validation split metrics in requested presentation units.

| model | Energy MAE | Energy RMSE | Forces MAE | Forces RMSE | source |
|---|---:|---:|---:|---:|---|
| MatterSim | 0.624206 | 1.009403 | 30.122465 | 49.921829 | `PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/water/mattersim/eval_valid.json` |
| MACE | 3.070448 | 3.419245 | 26.653249 | 55.606214 | `PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/water/mace/eval_valid.json` |
| MTP-16 | 3.901132 | 5.859228 | 333.057300 | 480.392500 | `FINAL_NEW_CHAT_CONTEXT_20260511/05_reports_metrics/results_handoff/final_metrics_wide.csv` |
| MTP-20 | 1.542203 | 2.560598 | 108.261100 | 191.793600 | `FINAL_NEW_CHAT_CONTEXT_20260511/05_reports_metrics/results_handoff/final_metrics_wide.csv` |


## 4. Unit conversion

- MatterSim/MACE energy values were read as `mae_E_per_atom_eV` and `rmse_E_per_atom_eV`, then multiplied by 1000 to obtain `meV/atom`.
- MatterSim/MACE force values were read as `mae_F_eV_A` and `rmse_F_eV_A`, then multiplied by 1000 to obtain `meV/Å`.
- MTP rows were read from final verified sources already normalized to `meV/atom` and `meV/Å`.

## 5. MTP anchor check

| model | metric | expected anchor | extracted | status |
|---|---|---:|---:|---|
| MTP-16 | energy_mae_meV_atom | 3.901132 | 3.901132 | PASS |
| MTP-16 | energy_rmse_meV_atom | 5.859228 | 5.859228 | PASS |
| MTP-16 | forces_mae_meV_A | 333.057300 | 333.057300 | PASS |
| MTP-16 | forces_rmse_meV_A | 480.392500 | 480.392500 | PASS |
| MTP-20 | energy_mae_meV_atom | 1.542203 | 1.542203 | PASS |
| MTP-20 | energy_rmse_meV_atom | 2.560598 | 2.560598 | PASS |
| MTP-20 | forces_mae_meV_A | 108.261100 | 108.261100 | PASS |
| MTP-20 | forces_rmse_meV_A | 191.793600 | 191.793600 | PASS |

## 6. Old water figure warning

The old `water_mae.png` and `water_rmse.png` figures in `presentation_full_context.zip` were not used as final metric sources. Their notebook provenance uses the old water MTP row labeled as level 16 and does not include the newer separate MTP-20 row from the final bundle. These figures are therefore suitable only for source discovery, not for final values or slide inputs.

## 7. Conflict table

| source | issue | decision |
|---|---|---|
| old water MTP files/figures from `presentation_full_context.zip` | filenames/job names suggest MTP-20, but metrics/script provenance identify level 16 | use final verified MTP-16 row from `final_metrics_wide.csv`; show MTP-20 separately from final bundle |
| final H2O MTP-20 source vs old water figures | old figures do not include separate final MTP-20 | ignore old figures for final values |

## 8. Output

- canonical CSV: `FINAL_NEW_CHAT_CONTEXT_20260511/05_reports_metrics/h2o_metrics_verified_20260511.csv`
- figure directory: `PRESENTATION/04_assets/figures/h2o/`
