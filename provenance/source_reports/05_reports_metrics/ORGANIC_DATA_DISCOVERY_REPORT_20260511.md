# ORGANIC DATA DISCOVERY REPORT 2026-05-11

## 1. Search Scope

Searched only inside the allowed presentation materials:

- `PRESENTATION/00_inbox/`
- `PRESENTATION/01_unpacked/`
- `PRESENTATION/03_content/`
- `PRESENTATION/04_assets/`

Archives inspected from `PRESENTATION/00_inbox/`:

- `presentation_full_context.zip`
- `final_training_bundle_20260510.zip`
- `protocols_eval_addendum_20260510.zip`

The search used only the listed presentation materials. It did not use raw datasets, checkpoints, model weights, training, or evaluation runs.

## 2. Candidate Files

| Path | Type | Models found | Temperatures found | Metrics found | Units found | Verified? | Decision |
|---|---|---|---|---|---|---|---|
| `PRESENTATION/00_inbox/presentation_full_context.zip::for_gpt/metrics/04_cross_temp_metrics_long.csv` | CSV | `MatterSim`, `MACE`, `MTP` levels 16/20 | `300K`, `600K`, `1200K` | Energy MAE/RMSE, Forces MAE/RMSE | `eV/atom`, `eV/A`, `meV/A` | yes | Used as normalized index and checked against JSON |
| `PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mace/test_*.json` | JSON | `MACE` | `300K`, `600K`, `1200K` | Energy MAE/RMSE per atom, Forces MAE/RMSE | `eV/atom`, `eV/A`, `meV/A` | yes | Used as source JSON |
| `PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mattersim/test_*.json` | JSON | `MatterSim` | `300K`, `600K`, `1200K` | Energy MAE/RMSE per atom, Forces MAE/RMSE | `eV/atom`, `eV/A`, `meV/A` | yes | Used as source JSON |
| `PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mtp/test_*_mtp16.json` | JSON | `MTP-16` | `300K`, `600K`, `1200K` | Energy MAE/RMSE per atom, Forces MAE/RMSE | `eV/atom`, `eV/A`, `meV/A` | yes | Used as source JSON |
| `PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mtp/test_*_mtp20.json` | JSON | `MTP-20` | `300K`, `600K`, `1200K` | Energy MAE/RMSE per atom, Forces MAE/RMSE | `eV/atom`, `eV/A`, `meV/A` | yes | Used as source JSON |
| `PRESENTATION/00_inbox/presentation_full_context.zip::19.03.26/cross_temp_eval_300_600_1200K_current/results/**/*.json` | JSON | same 4 model rows | `300K`, `600K`, `1200K` | same metric set | `eV/atom`, `eV/A`, `meV/A` | yes, duplicate | Not selected; values match preferred repo tree |
| `PRESENTATION/00_inbox/presentation_full_context.zip::for_gpt/metrics/04_cross_temp_summary.md` | Markdown summary | same 4 model rows | `300K`, `600K`, `1200K` | same metric set | `eV/atom`, `eV/A` | supporting summary | Used only for discovery/context |
| `PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/new_datasets/figures/cross_temp_organic.png` | PNG figure | inferred from filename/index only | inferred | no numeric table | none | no | Not used as metric source |
| `FINAL_NEW_CHAT_CONTEXT_20260511/01_handoff/NEW_CHAT_FINAL_HANDOFF_20260511.md` | Markdown handoff | model labels and claims | `300K`, `600K`, `1200K` | no complete numeric table | units mentioned | partial | Not used as numeric source |
| `FINAL_NEW_CHAT_CONTEXT_20260511/05_reports_metrics/results_handoff/final_metrics_long.csv` | CSV | water/alloy rows only | none for organic | no organic metrics | units for other datasets | yes, but incomplete | Not used for organic |
| `FINAL_NEW_CHAT_CONTEXT_20260511/05_reports_metrics/results_handoff/final_metrics_wide.csv` | CSV | water/alloy rows only | none for organic | no organic metrics | units for other datasets | yes, but incomplete | Not used for organic |
| `PRESENTATION/00_inbox/final_training_bundle_20260510.zip` | ZIP | water/alloy rows | none for organic | no organic metric table found | units for other datasets | yes, but not organic | Not used |
| `PRESENTATION/00_inbox/protocols_eval_addendum_20260510.zip` | ZIP | alloy protocol rows | none for organic | no organic metric table found | units for alloy protocols | yes, but not organic | Not used |

## 3. Verification Logic

The canonical table was built only from `repo_cross_temp_preferred` rows in `for_gpt/metrics/04_cross_temp_metrics_long.csv` inside `presentation_full_context.zip`.

For every canonical row:

- energy MAE/RMSE was taken from `energy_per_atom` rows in `eV/atom` and converted to `meV/atom`;
- forces MAE/RMSE was taken from `forces` rows in `meV/A`, reported as `meV/Å`;
- the row was checked against the corresponding JSON keys:
  - `mae_E_per_atom_eV`
  - `rmse_E_per_atom_eV`
  - `mae_F_meV_A`
  - `rmse_F_meV_A`
- the dated `19.03.26` duplicate rows were compared against the preferred repo rows and matched.

## 4. Found Values

| model_label | test_temperature | energy_mae_meV_atom | energy_rmse_meV_atom | forces_mae_meV_A | forces_rmse_meV_A | source JSON |
|---|---:|---:|---:|---:|---:|---|
| MatterSim | 300K | 0.668864347 | 0.842537021 | 32.542574670 | 45.489514842 | `repo/coursework/cross_temp_eval/results/mattersim/test_300K.json` |
| MatterSim | 600K | 1.144231636 | 1.451672159 | 57.434315622 | 83.203365310 | `repo/coursework/cross_temp_eval/results/mattersim/test_600K.json` |
| MatterSim | 1200K | 3.464716791 | 4.609007331 | 137.440116076 | 217.704820110 | `repo/coursework/cross_temp_eval/results/mattersim/test_1200K.json` |
| MACE | 300K | 0.569818976 | 0.678810855 | 18.569222160 | 25.892802761 | `repo/coursework/cross_temp_eval/results/mace/test_300K.json` |
| MACE | 600K | 0.953002409 | 1.208691746 | 33.851347442 | 49.835051013 | `repo/coursework/cross_temp_eval/results/mace/test_600K.json` |
| MACE | 1200K | 1.825729923 | 2.364865893 | 74.919010816 | 121.753520736 | `repo/coursework/cross_temp_eval/results/mace/test_1200K.json` |
| MTP-16 | 300K | 1.965594000 | 2.578954000 | 172.175900000 | 251.039200000 | `repo/coursework/cross_temp_eval/results/mtp/test_300K_mtp16.json` |
| MTP-16 | 600K | 4.677083000 | 6.495860000 | 256.605100000 | 375.815700000 | `repo/coursework/cross_temp_eval/results/mtp/test_600K_mtp16.json` |
| MTP-16 | 1200K | 14.777900000 | 20.442030000 | 441.936600000 | 748.242900000 | `repo/coursework/cross_temp_eval/results/mtp/test_1200K_mtp16.json` |
| MTP-20 | 300K | 1.632113000 | 2.099471000 | 140.196000000 | 205.931700000 | `repo/coursework/cross_temp_eval/results/mtp/test_300K_mtp20.json` |
| MTP-20 | 600K | 3.725958000 | 5.030732000 | 218.808800000 | 331.139900000 | `repo/coursework/cross_temp_eval/results/mtp/test_600K_mtp20.json` |
| MTP-20 | 1200K | 10.244110000 | 13.463010000 | 402.400300000 | 661.379600000 | `repo/coursework/cross_temp_eval/results/mtp/test_1200K_mtp20.json` |

## 5. Conflicts

No conflicts found. Preferred repo rows and dated duplicate rows match for the inspected organic metric keys.

## 6. Stage Decision

Complete verified organic metrics were found. The canonical 12-row table was created at:

- `FINAL_NEW_CHAT_CONTEXT_20260511/05_reports_metrics/organic_metrics_verified_20260511.csv`
