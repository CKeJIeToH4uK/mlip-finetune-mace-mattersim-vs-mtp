# New Datasets Results Summary

## Files inspected

| path | purpose | status | notes |
|---|---|---|---|
| `repo/coursework/new_datasets/water/` | H2O results/scripts/log pointers | inspected | Read eval JSON, MTP metrics, train/eval scripts/sbatch, selected stdout; skipped checkpoints/models/raw converted datasets. |
| `repo/coursework/new_datasets/alloy/` | MoNbTaVW results/scripts/log pointers | inspected | Read eval JSON, MTP metrics, train/eval scripts/sbatch, selected stdout; skipped checkpoints/models/raw converted datasets. |
| `repo/coursework/new_datasets/figures/` | figure inventory and notebook-linked provenance | inspected | Indexed PNG names/sizes/dimensions; did not use images as metric source. |
| `repo/coursework/new_datasets/analysis_v2.ipynb` | metadata/code/output inspection only | inspected | Notebook not executed. It has 29 cells, reads water/alloy/cross-temp JSON metrics and saves figures/*.png. |
| `repo/coursework/new_datasets/data/` | dataset file names and sizes only | inspected | Did not read dataset contents. Files: MoNbTaVW_train.json (7798699 bytes); MoNbTaVW_valid.json (1316397 bytes); dataset_1593.xyz (35629038 bytes); test_1200K.xyz (6437539 bytes); test_300K.cfg (5077098 bytes); test_300K.xyz (5023260 bytes); test_600K.xyz (6434399 bytes); train_300K.cfg (1508294 bytes); train_300K.xyz (1504880 bytes); train_H2O.cfg (24897782 bytes); valid_H2O.cfg (6285846 bytes) |

## Metric schema found

- MACE/MatterSim `eval_train.json` and `eval_valid.json` keys: `model_type`, `model_path`, `dataset_path`, `dataset_name`, `n_cfg`, `rmse_E_per_atom_eV`, `mae_E_per_atom_eV`, `rmse_F_eV_A`, `mae_F_eV_A`, `rmse_F_meV_A`, `mae_F_meV_A`, `time_sec_total`.
- MTP `metrics.json` / `metrics_20.json` keys: `dataset`, `species_order`, `level`, `train_db`, `valid_db`, `model_path`, `train_result`, `train_errors`, `valid_errors`.
- MTP numeric errors are stored inside raw `Errors (MAE, RMSE, MAXAE)` strings with rows `Energy`, `Energy/Atom`, `Forces`, `Stress`, `Charges`. P5 normalizes only `Energy`, `Energy/Atom`, and `Forces` MAE/RMSE.
- `analysis_v2.ipynb` uses these metric keys directly and converts energy-per-atom and force values to meV for several figures by multiplying by 1000.

## H2O / water results

### Energy MAE/RMSE

| model | variant | MTP level | train | valid | unit | source | notes |
|---|---|---:|---|---|---|---|---|
| MACE | fine-tuned | NA | MAE 0.00309929 / RMSE 0.00342747 | MAE 0.00307045 / RMSE 0.00341924 | eV/atom | `repo/coursework/new_datasets/water/mace/eval_train.json`; `repo/coursework/new_datasets/water/mace/eval_valid.json` | fine-tuned; MACE sbatch has multiheads_finetuning=False |
| MatterSim | fine-tuned | NA | MAE 0.000707521 / RMSE 0.00107355 | MAE 0.000624206 / RMSE 0.0010094 | eV/atom | `repo/coursework/new_datasets/water/mattersim/eval_train.json`; `repo/coursework/new_datasets/water/mattersim/eval_valid.json` | fine-tuned MatterSim |
| MTP | from-scratch | 16 | MAE 0.00414502 / RMSE 0.00608654 | MAE 0.00390113 / RMSE 0.00585923 | eV/atom | `repo/coursework/new_datasets/water/mtp/metrics.json` | from-scratch MTP parsed from raw Errors text; reported as level 16 by constructor/metrics; file/job names say mtp20 |

### Force MAE/RMSE

| model | variant | MTP level | train | valid | unit | source | notes |
|---|---|---:|---|---|---|---|---|
| MACE | fine-tuned | NA | MAE 0.0258527 / RMSE 0.0399326 | MAE 0.0266532 / RMSE 0.0556062 | eV/A | `repo/coursework/new_datasets/water/mace/eval_train.json`; `repo/coursework/new_datasets/water/mace/eval_valid.json` | fine-tuned; MACE sbatch has multiheads_finetuning=False |
| MatterSim | fine-tuned | NA | MAE 0.0305295 / RMSE 0.048269 | MAE 0.0301225 / RMSE 0.0499218 | eV/A | `repo/coursework/new_datasets/water/mattersim/eval_train.json`; `repo/coursework/new_datasets/water/mattersim/eval_valid.json` | fine-tuned MatterSim |
| MTP | from-scratch | 16 | MAE 0.3385 / RMSE 0.485187 | MAE 0.333057 / RMSE 0.480393 | eV/A | `repo/coursework/new_datasets/water/mtp/metrics.json` | from-scratch MTP parsed from raw Errors text; reported as level 16 by constructor/metrics; file/job names say mtp20 |

## MoNbTaVW / alloy results

### Energy MAE/RMSE

| model | variant | MTP level | train | valid | unit | source | notes |
|---|---|---:|---|---|---|---|---|
| MACE | fine-tuned | NA | MAE 0.0375128 / RMSE 0.0912319 | MAE 0.0347437 / RMSE 0.0644476 | eV/atom | `repo/coursework/new_datasets/alloy/mace/eval_train.json`; `repo/coursework/new_datasets/alloy/mace/eval_valid.json` | fine-tuned; MACE sbatch has multiheads_finetuning=False |
| MatterSim | fine-tuned | NA | MAE 0.00504458 / RMSE 0.0431958 | MAE 0.00684632 / RMSE 0.0289239 | eV/atom | `repo/coursework/new_datasets/alloy/mattersim/eval_train.json`; `repo/coursework/new_datasets/alloy/mattersim/eval_valid.json` | fine-tuned MatterSim |
| MTP | from-scratch | 16 | MAE 0.0138601 / RMSE 0.0420668 | MAE 0.0166934 / RMSE 0.0429538 | eV/atom | `repo/coursework/new_datasets/alloy/mtp/metrics.json` | from-scratch MTP parsed from raw Errors text; metrics.json level 16; current train.py is overwritten/level-20 version |
| MTP | from-scratch | 20 | MAE 0.00825637 / RMSE 0.0233157 | MAE 0.0129378 / RMSE 0.0396368 | eV/atom | `repo/coursework/new_datasets/alloy/mtp/metrics_20.json` | from-scratch MTP parsed from raw Errors text |

### Force MAE/RMSE

| model | variant | MTP level | train | valid | unit | source | notes |
|---|---|---:|---|---|---|---|---|
| MACE | fine-tuned | NA | MAE 0.0665674 / RMSE 0.0976057 | MAE 0.0706028 / RMSE 0.123247 | eV/A | `repo/coursework/new_datasets/alloy/mace/eval_train.json`; `repo/coursework/new_datasets/alloy/mace/eval_valid.json` | fine-tuned; MACE sbatch has multiheads_finetuning=False |
| MatterSim | fine-tuned | NA | MAE 0.0481441 / RMSE 0.0812949 | MAE 0.0547487 / RMSE 0.116898 | eV/A | `repo/coursework/new_datasets/alloy/mattersim/eval_train.json`; `repo/coursework/new_datasets/alloy/mattersim/eval_valid.json` | fine-tuned MatterSim |
| MTP | from-scratch | 16 | MAE 0.143239 / RMSE 0.215546 | MAE 0.148727 / RMSE 0.248981 | eV/A | `repo/coursework/new_datasets/alloy/mtp/metrics.json` | from-scratch MTP parsed from raw Errors text; metrics.json level 16; current train.py is overwritten/level-20 version |
| MTP | from-scratch | 20 | MAE 0.0922472 / RMSE 0.133254 | MAE 0.0944598 / RMSE 0.146763 | eV/A | `repo/coursework/new_datasets/alloy/mtp/metrics_20.json` | from-scratch MTP parsed from raw Errors text |

## MTP level consistency check

| area | path/job name says | script says | metrics says | safe level to write | notes |
|---|---|---|---|---|---|
| H2O / water MTP | `train.sbatch` job `water_mtp20`; model path `mtp20_trained.json`; script docstring says level 20 | constructor uses `MTP(..., level=16, ...)`; metrics dict writes `level: 16` | `metrics.json` has `level: 16`; stdout has object with `n_params = 222` and saves to `mtp20_trained.json` | `16` for numeric comparison, with naming caveat | Conflict is resolved for metrics as level 16, but filenames/job names remain misleading. |
| MoNbTaVW alloy MTP 16 | `metrics.json` model path `mtp16_trained.json`; stdout saves `mtp16_trained.json` but also prints a stale `MTP level 20` line | current `train.py` is level-20 version, likely overwritten after the level-16 run | `metrics.json` has `level: 16`; stdout object has `n_params = 897` | `16` | Use `metrics.json` as source of truth for this run; script provenance is not clean. |
| MoNbTaVW alloy MTP 20 | `train.sbatch` job `alloy_mtp20`; model path `mtp20_trained.json` | current `train.py` constructor uses `level=20` and prints level 20 | `metrics_20.json` has `level: 20`; stdout object has `n_params = 1293` | `20` | Consistent. |

## Figures

| path | likely content | source metrics known? | usable for final talk | notes |
|---|---|---|---|---|
| `repo/coursework/new_datasets/figures/alloy_mae.png` | MoNbTaVW train/valid MAE bars for energy and forces | known: analysis_v2.ipynb uses alloy_tr/alloy_val from eval JSON and alloy/mtp/metrics*.json | yes | 1776 x 738; 94255 bytes; generated/linked by analysis_v2.ipynb |
| `repo/coursework/new_datasets/figures/alloy_rmse.png` | MoNbTaVW train/valid RMSE bars for energy and forces | known: analysis_v2.ipynb uses alloy_tr/alloy_val from eval JSON and alloy/mtp/metrics*.json | yes | 1776 x 738; 94693 bytes; generated/linked by analysis_v2.ipynb |
| `repo/coursework/new_datasets/figures/cross_temp_organic.png` | Organic cross-temperature MAE energy/force trend | known from P4; analysis_v2.ipynb reads ../cross_temp_eval/results | yes | 2076 x 769; 139803 bytes; generated/linked by analysis_v2.ipynb |
| `repo/coursework/new_datasets/figures/loss_mace.png` | MACE training curves for H2O/alloy with MTP reference lines | partial: analysis_v2.ipynb parses MACE train.log and MTP metrics; exact log parser not fully audited in P5 | maybe | 2076 x 1474; 278239 bytes; generated/linked by analysis_v2.ipynb |
| `repo/coursework/new_datasets/figures/loss_mattersim.png` | MatterSim training curves for H2O/alloy with MTP reference lines | partial: analysis_v2.ipynb parses MatterSim train.log and MTP metrics; exact log parser not fully audited in P5 | maybe | 2076 x 1474; 218537 bytes; generated/linked by analysis_v2.ipynb |
| `repo/coursework/new_datasets/figures/mae_energy_all.png` | Overall MAE energy-per-atom comparison across organic, H2O and alloy | known: analysis_v2.ipynb reads cross_temp_eval/results plus water/alloy eval JSON and MTP metrics | yes | 1851 x 724; 59367 bytes; generated/linked by analysis_v2.ipynb |
| `repo/coursework/new_datasets/figures/mae_forces_all.png` | Overall MAE force comparison across organic, H2O and alloy | known: analysis_v2.ipynb reads cross_temp_eval/results plus water/alloy eval JSON and MTP metrics | yes | 1851 x 724; 59169 bytes; generated/linked by analysis_v2.ipynb |
| `repo/coursework/new_datasets/figures/rmse_energy_all.png` | Overall RMSE energy-per-atom comparison across organic, H2O and alloy | known: analysis_v2.ipynb reads cross_temp_eval/results plus water/alloy eval JSON and MTP metrics | yes | 1851 x 724; 60904 bytes; generated/linked by analysis_v2.ipynb |
| `repo/coursework/new_datasets/figures/rmse_forces_all.png` | Overall RMSE force comparison across organic, H2O and alloy | known: analysis_v2.ipynb reads cross_temp_eval/results plus water/alloy eval JSON and MTP metrics | yes | 1851 x 724; 60530 bytes; generated/linked by analysis_v2.ipynb |
| `repo/coursework/new_datasets/figures/water_mae.png` | H2O train/valid MAE bars for energy and forces | known: analysis_v2.ipynb uses water_tr/water_val from eval JSON and water/mtp/metrics.json | yes | 1776 x 738; 89154 bytes; generated/linked by analysis_v2.ipynb |
| `repo/coursework/new_datasets/figures/water_rmse.png` | H2O train/valid RMSE bars for energy and forces | known: analysis_v2.ipynb uses water_tr/water_val from eval JSON and water/mtp/metrics.json | yes | 1776 x 738; 80655 bytes; generated/linked by analysis_v2.ipynb |

## Presentation-ready takeaways

- On H2O, MatterSim has the lowest energy-per-atom MAE/RMSE on both train and valid splits: valid MAE/RMSE 0.000624 / 0.001009 eV/atom.
- On H2O, MACE has the lowest force MAE on both train and valid splits: valid force MAE/RMSE 0.026653 / 0.055606 eV/A.
- On H2O, MTP level 16 is close to MACE in energy MAE/RMSE but much worse on forces: valid force MAE/RMSE 0.333057 / 0.480393 eV/A.
- On MoNbTaVW, MatterSim has the lowest energy-per-atom MAE/RMSE on both train and valid splits: valid MAE/RMSE 0.006846 / 0.028924 eV/atom.
- On MoNbTaVW, MatterSim also has the lowest force MAE/RMSE on both train and valid splits: valid force MAE/RMSE 0.054749 / 0.116898 eV/A.
- On MoNbTaVW, MTP level 20 improves over MTP level 16 for both energy-per-atom and force metrics on train and valid splits.
- The local MACE fine-tuning scripts use `--multiheads_finetuning=False`, so final wording should be `fine-tuned MACE`, not multihead replay/LoRA/freeze.
- The notebook-generated figures are useful for presentation, but source-of-truth numbers should remain the normalized CSV/JSON metrics.

## Unclear / needs user decision

- Whether to show the H2O MTP naming conflict in the main deck or silently label numeric rows as MTP level 16 with a footnote.
- Whether to include total-energy MTP metrics (`Energy`, eV) in final slides, or show only `Energy/Atom` and `Forces`.
- Whether `loss_mace.png` and `loss_mattersim.png` should be included now or deferred until training-log parsing is separately normalized.
