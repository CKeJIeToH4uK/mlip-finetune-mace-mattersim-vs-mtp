# ORGANIC RESULTS SLIDES REPORT 2026-05-11

## 1. Discovery Summary

Verified organic cross-temperature metrics were found inside `PRESENTATION/00_inbox/presentation_full_context.zip`, normalized into the canonical 12-row CSV, and used for the MAE/RMSE result slides. The organic block now has four standalone preview pages: training dynamics, MTP ensemble sanity check, MAE setup/results, and RMSE takeaways.

The slide block uses only the listed source files. It does not use raw datasets, checkpoints, model weights, rerun training/evaluation outputs, external sources, OCR-derived values, or reconstructed metric values.

## 2. Candidate Source Files

| Source | Role | Status |
|---|---|---|
| `PRESENTATION/00_inbox/presentation_full_context.zip::for_gpt/metrics/04_cross_temp_metrics_long.csv` | normalized organic metrics index | used for canonical metrics |
| `PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mace/test_*.json` | MACE source metrics | used |
| `PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mattersim/test_*.json` | MatterSim source metrics | used |
| `PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mtp/test_*_mtp16.json` | MTP-16 source metrics | used |
| `PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mtp/test_*_mtp20.json` | MTP-20 source metrics | used |
| `PRESENTATION/00_inbox/presentation_full_context.zip::26.02.26/epoch_vs_err_curve.csv` | MatterSim organic learning curve | used for training dynamics |
| `PRESENTATION/00_inbox/presentation_full_context.zip::26.02.26/mace_finetune/ft_300K/results/ft_300K_run-42_train.txt` | MACE organic learning curve | used for training dynamics |
| `PRESENTATION/00_inbox/presentation_full_context.zip::26.02.26/mace_finetune/ft_300K/train.log` | MACE learning-curve provenance | checked |
| `PRESENTATION/00_inbox/presentation_full_context.zip::26.02.26/mattersim_finetune/epoch_vs_err/train.log` | MatterSim learning-curve provenance | checked |
| `PRESENTATION/00_inbox/presentation_full_context.zip::26.02.26/logs_16/mtp_train_*.out` | MTP numeric traces | rejected for plotting: unlabeled y-axis metric |
| `PRESENTATION/00_inbox/presentation_full_context.zip::26.02.26/logs_20/mtp_train_*.out` | MTP numeric traces | rejected for plotting: unlabeled y-axis metric |
| `PRESENTATION/00_inbox/presentation_full_context.zip::26.02.26/mtp_errors_summary.csv` | MTP final train/validation errors | rejected as learning curve: no epoch/step series |
| `PRESENTATION/03_content/ensemble_aggregates_verified_20260511.csv` | MTP repeated-run train/validation aggregates | used for MTP ensemble sanity check |
| `FINAL_NEW_CHAT_CONTEXT_20260511/05_reports_metrics/organic_metrics_verified_20260511.csv` | current organic single-run cross-temperature metrics | used for MTP single-run markers |

Full metric discovery details are in `PRESENTATION/03_content/ORGANIC_DATA_DISCOVERY_REPORT_20260511.md`.

Learning-curve discovery details are in `PRESENTATION/03_content/ORGANIC_LEARNING_CURVES_DISCOVERY_20260511.md`.

## 3. Final Verified Organic Table

Canonical CSV:

- `FINAL_NEW_CHAT_CONTEXT_20260511/05_reports_metrics/organic_metrics_verified_20260511.csv`

Schema:

```text
dataset,model_label,test_temperature,split,energy_mae_meV_atom,energy_rmse_meV_atom,forces_mae_meV_A,forces_rmse_meV_A,source_file,notes
```

The table has the expected 12 rows:

- 4 models: `MatterSim`, `MACE`, `MTP-16`, `MTP-20`;
- 3 test temperatures: `300K`, `600K`, `1200K`;
- complete Energy MAE/RMSE and Forces MAE/RMSE values.

Energy units: `meV/atom`. Force units: `meV/Å`.

## 4. Figure List

Organic metric figures are reused from the canonical CSV. All use line plots with markers and linear y-scale.

| Path | Metric | Units | Y-scale |
|---|---|---|---|
| `PRESENTATION/04_assets/figures/organic/organic_energy_mae.pdf` | Energy MAE | `meV/atom` | linear |
| `PRESENTATION/04_assets/figures/organic/organic_energy_mae.png` | Energy MAE | `meV/atom` | linear |
| `PRESENTATION/04_assets/figures/organic/organic_forces_mae.pdf` | Forces MAE | `meV/Å` | linear |
| `PRESENTATION/04_assets/figures/organic/organic_forces_mae.png` | Forces MAE | `meV/Å` | linear |
| `PRESENTATION/04_assets/figures/organic/organic_energy_rmse.pdf` | Energy RMSE | `meV/atom` | linear |
| `PRESENTATION/04_assets/figures/organic/organic_energy_rmse.png` | Energy RMSE | `meV/atom` | linear |
| `PRESENTATION/04_assets/figures/organic/organic_forces_rmse.pdf` | Forces RMSE | `meV/Å` | linear |
| `PRESENTATION/04_assets/figures/organic/organic_forces_rmse.png` | Forces RMSE | `meV/Å` | linear |

Learning-dynamics figures created:

| Path | Metric | Units | Y-scale |
|---|---|---|---|
| `PRESENTATION/04_assets/figures/organic_learning/organic_learning_universal.pdf` | MatterSim train/validation loss; MACE validation loss | dimensionless loss | log, explicitly labeled |
| `PRESENTATION/04_assets/figures/organic_learning/organic_learning_universal.png` | MatterSim train/validation loss; MACE validation loss | dimensionless loss | log, explicitly labeled |

Learning-figure script:

- `PRESENTATION/03_content/make_organic_learning_curves_20260511.py`

Organic ensemble figure:

| Path | Metric | Units | Y-scale |
|---|---|---|---|
| `PRESENTATION/04_assets/figures/organic_ensemble/organic_mtp_ensemble_sanity.pdf` | MTP validation Energy MAE and Forces MAE: ensemble mean ± std plus single-run marker | `meV/atom`, `meV/Å` | linear |
| `PRESENTATION/04_assets/figures/organic_ensemble/organic_mtp_ensemble_sanity.png` | MTP validation Energy MAE and Forces MAE: ensemble mean ± std plus single-run marker | `meV/atom`, `meV/Å` | linear |

## 5. Slide Table

| Deck slide number | Namespace | File | Title | Figures used | Main message |
|---:|---|---|---|---|---|
| 24 | `res_02a_organic_training_dynamics` | `PRESENTATION/05_deck/sections/res_02a_organic_training_dynamics.tex` | Organic: кривые обучения | `organic_learning_universal.pdf` | Curves are an optimization/provenance sanity check, not final ranking |
| 25 | `res_02b_organic_mtp_ensemble_sanity` | `PRESENTATION/05_deck/sections/res_02b_organic_mtp_ensemble_sanity.tex` | Organic: ансамбль MTP на 300K | `organic_mtp_ensemble_sanity.pdf` | MTP single-run MAE values are close to the 300K validation ensemble mean; later 600K/1200K results remain single-run only |
| 26 | `res_02_organic_setup_results` | `PRESENTATION/05_deck/sections/res_02_organic_setup_results.tex` | Organic: перенос от 300K к более высоким температурам | Energy MAE, Forces MAE | Setup and MAE comparison for train 300K to test 300K/600K/1200K |
| 27 | `res_03_organic_takeaway` | `PRESENTATION/05_deck/sections/res_03_organic_takeaway.tex` | Organic: основной вывод | Energy RMSE, Forces RMSE | RMSE confirmation and compact organic-specific takeaways |

Registry:

- `PRESENTATION/05_deck/sections/05_organic_results.tex`

Standalone preview:

- `PRESENTATION/05_deck/main_organic_results_preview.tex`

## 6. Claim-Source Map

| Claim | Source |
|---|---|
| train/test setup is train 300K and test 300K/600K/1200K | source JSON `dataset_name` fields and `for_gpt/metrics/04_cross_temp_summary.md` inside `presentation_full_context.zip` |
| included labels are `MatterSim`, `MACE`, `MTP-16`, `MTP-20` | `organic_metrics_verified_20260511.csv` |
| plotted metrics are Energy MAE/RMSE and Forces MAE/RMSE | source JSON keys and canonical CSV columns |
| energy unit is `meV/atom` | eV/atom source values converted by multiplying by 1000 |
| force unit is `meV/Å` | source `meV/A` force rows, rendered as `meV/Å` |
| MACE and MatterSim have lower MAE than MTP baselines on organic test temperatures | canonical Energy MAE and Forces MAE rows |
| MACE is best among current organic rows | canonical table: lowest values for all four metrics at all three temperatures |
| MatterSim is also below MTP baselines | canonical table: MatterSim values are below MTP-16 and MTP-20 values for all four metrics at all three temperatures |
| MTP-20 improves MTP-16 but does not close the gap | canonical table: MTP-20 values are below MTP-16 values, but above MACE/MatterSim values |
| learning curves are optimization/provenance evidence only | accepted numeric training logs plus explicit caveat on slide 24 |
| MTP learning traces were not plotted | discovery report: MTP traces have unlabeled y-axis metric, and summary file has no curve |
| MTP-16/MTP-20 have five repeated train/validation 300K runs | `ensemble_aggregates_verified_20260511.csv`, rows with `dataset=organic`, `split=valid_300K`, `n_runs=5` |
| single-run MTP 300K validation MAE falls within one sample standard deviation of the ensemble mean | Energy MAE and Forces MAE differences between `organic_metrics_verified_20260511.csv` 300K single-run rows and `ensemble_aggregates_verified_20260511.csv` validation means are within one sample standard deviation for both MTP levels |

All result claims are scoped to the organic cross-temperature block.

## 7. Learning Curves Addition

Discovery summary:

- MatterSim learning curves were found in `26.02.26/epoch_vs_err_curve.csv` with 500 train points and 500 validation points over epochs 0--499.
- MACE validation loss was found in `26.02.26/mace_finetune/ft_300K/results/ft_300K_run-42_train.txt` with 500 validation points over epochs 0--499.
- MTP logs contain numeric traces, but the trace y-axis metric is not labeled clearly enough to plot honestly.

Figures created:

- `PRESENTATION/04_assets/figures/organic_learning/organic_learning_universal.pdf`
- `PRESENTATION/04_assets/figures/organic_learning/organic_learning_universal.png`

New slide:

- `PRESENTATION/05_deck/sections/res_02a_organic_training_dynamics.tex`

Caveat:

- Loss definitions differ across protocols, so curves are used only to show training/evaluation provenance and optimization sanity, not final model ranking.

## 8. Organic MTP Ensemble Sanity Check

Source files used:

- `PRESENTATION/03_content/ensemble_aggregates_verified_20260511.csv`
- `FINAL_NEW_CHAT_CONTEXT_20260511/05_reports_metrics/organic_metrics_verified_20260511.csv`
- `FINAL_NEW_CHAT_CONTEXT_20260511/05_reports_metrics/ENSEMBLE_AUDIT_REPORT_20260511.md`
- `FINAL_NEW_CHAT_CONTEXT_20260511/05_reports_metrics/ENSEMBLE_PLOTTING_POLICY_20260511.md`

Repeated-run coverage:

- `MTP-16`: `n_runs=5` for organic `valid_300K`;
- `MTP-20`: `n_runs=5` for organic `valid_300K`.

Metrics shown on the slide:

- Energy MAE, `meV/atom`;
- Forces MAE, `meV/Å`.

Displayed MAE comparison:

| Level | Metric | Ensemble mean | Ensemble std | Single-run value | Within 1 std |
|---|---|---:|---:|---:|---|
| MTP-16 | Energy MAE | 2.160216 | 0.356923 | 1.965594 | yes |
| MTP-16 | Forces MAE | 178.738120 | 37.297262 | 172.175900 | yes |
| MTP-20 | Energy MAE | 1.873388 | 0.282846 | 1.632113 | yes |
| MTP-20 | Forces MAE | 152.027960 | 21.998949 | 140.196000 | yes |

Chosen slide wording:

- `Одиночный запуск MTP для 300K validation находится в пределах одного выборочного стандартного отклонения от среднего ансамбля по MAE.`
- `Для 600K/1200K далее показана доступная оценка по одному запуску.`

Reason:

- The slide shows only MAE, and the displayed single-run MAE markers are within one sample standard deviation of the corresponding 300K validation ensemble mean for both MTP levels.

Caveat:

- `mean ± std` is shown only for 300K validation; the 600K/1200K spread is not inferred or transferred, and no aggregation is performed across MTP levels or splits.

Language/layout cleanup:

- Slide title changed to `Organic: ансамбль MTP на 300K`.
- The figure caption was translated to Russian.
- The extra in-figure `lower is better` text and duplicate 600K/1200K caveat were removed.

## 9. Build Status

Commands used:

```bash
python3 PRESENTATION/03_content/make_organic_learning_curves_20260511.py
cd PRESENTATION/05_deck
mkdir -p ../06_build/latex_aux/previews/organic_results
xelatex -interaction=nonstopmode -halt-on-error -output-directory=../06_build/latex_aux/previews/organic_results main_organic_results_preview.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=../06_build/latex_aux/previews/organic_results main_organic_results_preview.tex
cp ../06_build/latex_aux/previews/organic_results/main_organic_results_preview.pdf ../06_build/main_organic_results_preview.pdf
rm -rf ../06_build/organic_results_preview
mkdir -p ../06_build/organic_results_preview
pdftoppm -png ../06_build/main_organic_results_preview.pdf ../06_build/organic_results_preview/organic_results
```

Status:

- learning figure generation: success;
- organic ensemble figure regeneration: success;
- LaTeX build: success;
- PDF pages: 4;
- PNG previews: success.

Produced preview:

- `PRESENTATION/06_build/main_organic_results_preview.pdf`
- `PRESENTATION/06_build/organic_results_preview/organic_results-01.png`
- `PRESENTATION/06_build/organic_results_preview/organic_results-02.png`
- `PRESENTATION/06_build/organic_results_preview/organic_results-03.png`
- `PRESENTATION/06_build/organic_results_preview/organic_results-04.png`
- `PRESENTATION/06_build/organic_results_preview/organic_results-1.png`
- `PRESENTATION/06_build/organic_results_preview/organic_results-2.png`
- `PRESENTATION/06_build/organic_results_preview/organic_results-3.png`
- `PRESENTATION/06_build/organic_results_preview/organic_results-4.png`

PDF page check:

```text
Pages:           4
Page size:       453.54 x 255.12 pts
```

Rendered review:

- page 1 is Organic learning curves;
- page 2 is Organic MTP ensemble sanity check;
- page 3 is Organic MAE results;
- page 4 is Organic RMSE + takeaway;
- page 1 has one centered learning-dynamics figure, no right-side text boxes, and a compact Russian caveat;
- page 2 has centered MTP MAE panels, Russian caption, no duplicate caveat, and no `lower is better` annotation;
- pages 3 and 4 still contain exactly two metric plots each;
- existing organic metric figures render correctly;
- no overfull box appears in the final LaTeX log.

## 10. Compliance Checks

Canonical CSV was not edited in this task:

```text
4965ae180abe8d15239b0a34d5936e5d788524fb157834e330ebb2f8d681564e  FINAL_NEW_CHAT_CONTEXT_20260511/05_reports_metrics/organic_metrics_verified_20260511.csv
```

Forbidden-term check on organic slide/preview files:

```text
no matches
```

Required labels in organic slide files:

```text
MatterSim: present
MACE: present
MTP-16: present
MTP-20: present
```

Required units in organic metric slides:

```text
meV/atom: present
meV/Å: present
```

Git status from presentation workspace:

```text
fatal: not a git repository (or any of the parent directories): .git
```

The presentation workspace is not covered by the discovered `repo/.git`, so `git status` and normal `git diff` are unavailable for these files. The diff artifact was produced with `git diff --no-index`.

Protected files not modified by this task:

- `PRESENTATION/05_deck/main.tex`
- `PRESENTATION/05_deck/sections/prearch_*.tex`
- `PRESENTATION/05_deck/sections/arch_*.tex`
- `PRESENTATION/05_deck/sections/04_results_intro.tex`
- `PRESENTATION/05_deck/sections/res_01_experimental_setup.tex`
- `PRESENTATION/03_content/results_handoff/*`

## 11. Warnings / Conflicts

No metric conflicts found.

No MTP learning-curve figure was created because the available MTP iteration traces do not provide a clear y-axis metric label. This is not a blocker for the organic result slides because MTP-16/MTP-20 remain compared by the verified held-out test metrics on slides 26--27.

Non-blocking build warnings from the existing HSE template remain in the log about internal logo image declarations, but the rendered preview shows the template and the build succeeds.

## 12. Integration Note

The block is standalone and was not integrated into `main.tex`.

After review, it can be integrated after:

```tex
\input{sections/04_results_intro}
```

by adding:

```tex
\input{sections/05_organic_results}
```

Integration was not performed.

## 13. Diff

Diff saved to:

- `PRESENTATION/03_content/ORGANIC_RESULTS_SLIDES_DIFF_20260511.patch`
