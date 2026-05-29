# Alloy MTP-16 audit report, 2026-05-11

## Search root used

`repo/coursework`

Root selection followed the requested order. `/home/brmannanov/coursework` was not present locally; `repo/coursework` was present and used.

Report output:

`FINAL_NEW_CHAT_CONTEXT_20260511/05_reports_metrics/ALLOY_MTP16_AUDIT_REPORT_20260511.md`

Canonical MTP-16 metrics CSV:

`FINAL_NEW_CHAT_CONTEXT_20260511/05_reports_metrics/alloy_mtp16_audit_metrics_20260511.csv`

## Commands and search method used

Read-only search and inspection only. No training or evaluation commands were run.

- `find . -maxdepth 3 -type d` to map likely directories.
- `rg --files | rg -i '(MTP-?16|mtp16|level_?16|MTP-?20|mtp20|MoNbTaVW|alloy|NbMo|MoNb|TaVW|metrics|results|eval|valid|train)'` to find candidate paths.
- `rg -n -i '(MoNbTaVW|alloy|NbMo|MoNb|TaVW|MTP-?16|mtp16|level_?16|MTP-?20|mtp20|level_?20|Energy MAE|Energy RMSE|Forces MAE|Forces RMSE|energy_mae|energy_rmse|forces_mae|forces_rmse|meV/atom|eV/atom|eV/A)'` over text-like file types.
- `jq` on candidate JSON metrics/model files to inspect keys, `level`, `dataset`, `species_order`, `train_db`, `valid_db`, `model_path`, parameter count, and basis length.
- `rg` on candidate logs and scripts to inspect level strings, model paths, saved metrics paths, and dataset paths.

## Candidate directories found

| directory | relevance | status |
|---|---|---|
| `new_datasets/alloy/mtp` | Contains alloy MTP model files, metrics, logs, and train script. | Accepted for MoNbTaVW MTP-16 and MTP-20. |
| `new_datasets/alloy/convert` | Contains `train_alloy`/`valid_alloy`; conversion log mentions `MoNbTaVW_train.json` and `MoNbTaVW_valid.json`. | Accepted as MoNbTaVW dataset evidence. |
| `mtp_runs/level16_run1` | Contains MTP-16 model and metrics. | Rejected for alloy: species/order and paths are organic H/C/N/O. |
| `mtp_runs/level20_run1` | Contains MTP-20 model and metrics. | Rejected for alloy: species/order and paths are organic H/C/N/O. |
| `cross_temp_eval/results/mtp` | Contains MTP-16/MTP-20 eval JSON files. | Rejected for alloy: points to old `mtp_runs` organic models and organic temperature datasets. |
| `initial_eval/results/mtp_init` | Contains random/init MTP-20 metrics. | Rejected: organic H/C/N/O and not alloy. |
| `new_datasets/water/mtp` | Contains water MTP metrics and model. | Rejected: dataset is `water_H2O`. |

## Candidate model files found

| path | why relevant | dataset inferred | level inferred | evidence | status |
|---|---|---|---|---|---|
| `new_datasets/alloy/mtp/mtp16_trained.json` | Filename/path indicate alloy MTP-16. | MoNbTaVW/alloy | 16 | Model `species_order=[23,41,42,73,74]`; `params` length 897; `mtp_basis.basis_functions` length 122, matching level-16 basis shape seen in old level-16 model; paired metrics file has `level=16`. | Accepted. |
| `new_datasets/alloy/mtp/mtp20_trained.json` | MTP-20 comparison model. | MoNbTaVW/alloy | 20 | Model `species_order=[23,41,42,73,74]`; `params` length 1293; `mtp_basis.basis_functions` length 390; metrics file has `level=20`. | Accepted for MTP-20 comparison. |
| `mtp_runs/level16_run1/mtp16_trained.json` | Filename/path indicate MTP-16. | Organic, not alloy | 16 | Metrics and model species are `[1,6,7,8]` / H,C,N,O; train/valid paths under `databases/train_300K_from_xyz.json` and `test_300K_from_xyz.json`. | Rejected for alloy. |
| `mtp_runs/level20_run1/mtp20_trained.json` | Filename/path indicate MTP-20. | Organic, not alloy | 20 | Metrics and model species are `[1,6,7,8]` / H,C,N,O. | Rejected for alloy. |
| `initial_eval/results/mtp_init/mtp_init_level20.json` | MTP init model. | Organic, not alloy | 20 | Metrics species are `[1,6,7,8]`; model is random/init. | Rejected. |
| `new_datasets/water/mtp/mtp20_trained.json` | MTP file with misleading name. | H2O/water | 16 by metrics/model basis; filename says mtp20 | Metrics `dataset=water_H2O`, `level=16`, `species_order=[1,8]`. | Rejected for alloy. |

## Candidate metric files found

| path | why relevant | dataset inferred | actual level | split available | metrics available | source units | accepted/rejected | reason |
|---|---|---|---:|---|---|---|---|---|
| `new_datasets/alloy/mtp/metrics.json` | Main MTP-16 alloy metrics candidate. | MoNbTaVW/alloy | 16 | train, valid | Energy/Atom MAE/RMSE; Forces MAE/RMSE | eV/atom and eV/A in MTP error strings; converted to meV units | Accepted | `dataset=alloy_MoNbTaVW`; `train_db=train_alloy.json`; `valid_db=valid_alloy.json`; species V,Nb,Mo,Ta,W; model path `mtp16_trained.json`. |
| `new_datasets/alloy/mtp/metrics_20.json` | MTP-20 alloy comparison metrics. | MoNbTaVW/alloy | 20 | train, valid | Energy/Atom MAE/RMSE; Forces MAE/RMSE | eV/atom and eV/A in MTP error strings; converted to meV units | Accepted for MTP-20 comparison | Matches expected handoff values within rounding. |
| `mtp_runs/level16_run1/metrics.json` | MTP-16 metrics candidate by name. | Organic, not alloy | 16 | train, valid | Energy/Atom MAE/RMSE; Forces MAE/RMSE | eV/atom and eV/A | Rejected | Species are H,C,N,O; no MoNbTaVW/alloy evidence. |
| `mtp_runs/level20_run1/metrics.json` | MTP-20 metrics candidate by name. | Organic, not alloy | 20 | train, valid | Energy/Atom MAE/RMSE; Forces MAE/RMSE | eV/atom and eV/A | Rejected | Species are H,C,N,O; no MoNbTaVW/alloy evidence. |
| `cross_temp_eval/results/mtp/test_300K_mtp16.json` | MTP-16 result JSON. | Organic, not alloy | 16 by model name/path | test | Energy per atom MAE/RMSE; Forces MAE/RMSE | eV/atom and meV/A keys | Rejected | Points to `mtp_runs/level16_run1`, not alloy. |
| `cross_temp_eval/results/mtp/test_600K_mtp16.json` | MTP-16 result JSON. | Organic, not alloy | 16 by model name/path | test | Energy per atom MAE/RMSE; Forces MAE/RMSE | eV/atom and meV/A keys | Rejected | Points to `mtp_runs/level16_run1`, not alloy. |
| `cross_temp_eval/results/mtp/test_1200K_mtp16.json` | MTP-16 result JSON. | Organic, not alloy | 16 by model name/path | test | Energy per atom MAE/RMSE; Forces MAE/RMSE | eV/atom and meV/A keys | Rejected | Points to `mtp_runs/level16_run1`, not alloy. |
| `cross_temp_eval/results/mtp/test_300K_mtp20.json`, `test_600K_mtp20.json`, `test_1200K_mtp20.json` | MTP-20 result JSON files. | Organic, not alloy | 20 by model name/path | test | Energy per atom MAE/RMSE; Forces MAE/RMSE | eV/atom and meV/A keys | Rejected | Point to `mtp_runs/level20_run1`, not alloy. |
| `initial_eval/results/mtp_init/mtp_init_eval.json` | MTP init metrics. | Organic, not alloy | 20 | train, valid | Energy/Atom MAE/RMSE; Forces MAE/RMSE | eV/atom and eV/A | Rejected | Random/init model; species H,C,N,O. |
| `new_datasets/water/mtp/metrics.json` | MTP metrics with filename mismatch. | H2O/water | 16 | train, valid | Energy/Atom MAE/RMSE; Forces MAE/RMSE | eV/atom and eV/A | Rejected | `dataset=water_H2O`; not alloy. |

## Candidate logs found

| path | why relevant | dataset inferred | level evidence | accepted/rejected | reason |
|---|---|---|---|---|---|
| `new_datasets/alloy/mtp/alloy_mtp16_3813991.out` | Saved `mtp16_trained.json` and `metrics.json`. | MoNbTaVW/alloy by path, output files, metrics pairing | Prints `MTP level 20: 897 parameters, 5 species`; saved model path is `mtp16_trained.json`; metrics says `level=16`; model basis length is 122. | Accepted with mismatch note | The `level 20` print conflicts with stronger file/metrics/model evidence and parameter count. Actual level classified as 16. |
| `new_datasets/alloy/mtp/alloy_mtp20_3814067.out` | Saved `mtp20_trained.json` and `metrics_20.json`. | MoNbTaVW/alloy | Prints `MTP level 20: 1293 parameters, 5 species`; saved metrics path is `metrics_20.json`. | Accepted for MTP-20 comparison | Consistent with metrics/model. |
| `new_datasets/alloy/mtp/alloy_mtp20_3813826.out` | MTP-20 log by name. | MoNbTaVW/alloy by path | Only confirms `MTP level 20: 1293 parameters, 5 species`; no saved metrics line in inspected output. | Rejected as duplicate/incomplete evidence | Later `alloy_mtp20_3814067.out` plus `metrics_20.json` are complete. |
| `mtp_runs/level16_run1/slurm_3731605.out` | Old MTP-16 log. | Organic, not alloy | `n_params=608`, species H,C,N,O; saved `mtp16_trained.json`. | Rejected for alloy | Not MoNbTaVW. |
| `mtp_runs/level20_run1/slurm_3731609.out` | Old MTP-20 log. | Organic, not alloy | `n_params=932`, species H,C,N,O; saved `mtp20_trained.json`. | Rejected for alloy | Not MoNbTaVW. |
| `cross_temp_eval/slurm_logs/eval_mtp_*.out` | MTP eval logs. | Organic, not alloy | Model paths point to old `mtp_runs` level16/level20. | Rejected for alloy | Cross-temperature organic evaluation, not MoNbTaVW. |
| `new_datasets/water/mtp/water_mtp20_*.out` | Water MTP logs. | H2O/water | Water path and metrics. | Rejected | Not alloy. |

## Stage B: level verification

Verified MoNbTaVW MTP-16 candidate:

- Folder/model name: `new_datasets/alloy/mtp/mtp16_trained.json`.
- Metrics JSON: `new_datasets/alloy/mtp/metrics.json` has `level=16`.
- Dataset metadata: `dataset=alloy_MoNbTaVW`.
- Model JSON: no explicit `level` field, but `species_order=[23,41,42,73,74]`, `params` length 897, `mtp_basis.basis_functions` length 122.
- Cross-check: old verified level-16 organic model also has basis length 122; level-20 models have basis length 390.
- Log mismatch: `alloy_mtp16_3813991.out` prints `MTP level 20: 897 parameters, 5 species`, but saves `mtp16_trained.json`/`metrics.json`. The `897` parameter count and 122 basis length support actual level 16.

Classification: `actual_level=16`, with a logged-level print mismatch recorded.

Verified MoNbTaVW MTP-20 candidate:

- Metrics JSON: `new_datasets/alloy/mtp/metrics_20.json` has `level=20`.
- Model JSON: `params` length 1293, `mtp_basis.basis_functions` length 390.
- Log: `alloy_mtp20_3814067.out` prints `MTP level 20: 1293 parameters, 5 species`.

Classification: `actual_level=20`.

## Stage C: dataset verification

MoNbTaVW/alloy evidence for accepted MTP-16:

- `new_datasets/alloy/mtp/metrics.json` has `dataset=alloy_MoNbTaVW`.
- `train_db=/home/brmannanov/coursework/new_datasets/alloy/convert/train_alloy.json`.
- `valid_db=/home/brmannanov/coursework/new_datasets/alloy/convert/valid_alloy.json`.
- Species/order visible as `[23,41,42,73,74]`, matching V, Nb, Mo, Ta, W.
- Conversion evidence in `new_datasets/alloy/convert/alloy_convert_3813821.out`: `MoNbTaVW_train.json -> train_alloy.xyz` and `MoNbTaVW_valid.json -> valid_alloy.xyz`.
- Converter comments map MoNbTaVW types to V, Nb, Mo, Ta, W.

Rejected non-alloy evidence:

- Old `mtp_runs/*` use H,C,N,O species.
- `new_datasets/water/mtp/*` uses `water_H2O` and H/O species.
- `cross_temp_eval/results/mtp/*` points to old organic `mtp_runs` models.

## Stage D: extracted verified MTP-16 metrics

Source: `new_datasets/alloy/mtp/metrics.json`.

Source strings use `Energy/Atom` and `Forces` in eV/atom and eV/A. Values below are converted to meV/atom and meV/A.

| dataset | model | actual level | split | Energy MAE | Energy RMSE | Forces MAE | Forces RMSE | source |
|---|---|---:|---|---:|---:|---:|---:|---|
| alloy_MoNbTaVW | MTP-16 | 16 | train | 13.860 | 42.067 | 143.240 | 215.546 | `new_datasets/alloy/mtp/metrics.json` |
| alloy_MoNbTaVW | MTP-16 | 16 | valid | 16.693 | 42.954 | 148.727 | 248.981 | `new_datasets/alloy/mtp/metrics.json` |

Canonical CSV created:

`FINAL_NEW_CHAT_CONTEXT_20260511/05_reports_metrics/alloy_mtp16_audit_metrics_20260511.csv`

## Stage E: comparison to existing MTP-20

Source: `new_datasets/alloy/mtp/metrics_20.json`.

| model | split | Energy MAE | Energy RMSE | Forces MAE | Forces RMSE | source |
|---|---|---:|---:|---:|---:|---|
| MTP-16 | train | 13.860 | 42.067 | 143.240 | 215.546 | `new_datasets/alloy/mtp/metrics.json` |
| MTP-16 | valid | 16.693 | 42.954 | 148.727 | 248.981 | `new_datasets/alloy/mtp/metrics.json` |
| MTP-20 | train | 8.256 | 23.316 | 92.247 | 133.254 | `new_datasets/alloy/mtp/metrics_20.json` |
| MTP-20 | valid | 12.938 | 39.637 | 94.460 | 146.763 | `new_datasets/alloy/mtp/metrics_20.json` |

MTP-20 conflict check:

- Expected handoff valid Energy MAE: approximately 12.938 meV/atom. Found 12.93780.
- Expected handoff valid Energy RMSE: approximately 39.637 meV/atom. Found 39.63677.
- Expected handoff valid Forces MAE: approximately 94.460 meV/A. Found 94.45979.
- Expected handoff valid Forces RMSE: approximately 146.763 meV/A. Found 146.76340.

No conflict with the handoff values; differences are rounding only.

## Final decision for alloy slides

`INCLUDE MTP-16`

Verified MoNbTaVW MTP-16 validation metrics were found; actual level is verified as 16 from metrics and model basis/parameter evidence; units are clear and converted.

Recommendation: Add MTP-16 to MoNbTaVW main comparison alongside MatterSim, MACE-EW50, MTP-20.

Important caveat for notes/source tracking: the MTP-16 log contains a conflicting line `MTP level 20: 897 parameters, 5 species`; report it as a log print mismatch, not as actual level 20.
