# Final Training Bundle 20260510

Purpose:
This bundle gives the presentation builder a compact, self-contained context for the final computations before the May 13 defense of КР_МОП_РЕГРЕССИЯ.

Included:
- Clean H2O MTP-20 scripts, logs, metrics JSON/CSV.
- Old H2O MTP folder context, labeled as MTP-16 because metrics.json has level=16.
- Old MACE alloy baseline.
- MACE alloy lr=1e-3 quick250 and fair200 checks.
- Final MACE alloy EW10/EW50 normal-partition runs.
- Optional protocol ablation scripts/status where available.
- Generated normalized metrics tables and presentation caveats.

Intentionally excluded:
- raw/converted train/valid datasets;
- MACE/MTP model files;
- checkpoints and model directories;
- *.model, *.pt, *.pth, raw *.xyz files;
- hidden caches and __pycache__.

Source folders:
- repo/coursework/new_datasets/water/mtp_clean20_20260508
- repo/coursework/new_datasets/water/mtp
- repo/coursework/new_datasets/alloy/mace
- repo/coursework/new_datasets/alloy/mace_retrain_lr0p001_quick3h_20260509
- repo/coursework/new_datasets/alloy/mace_retrain_lr0p001_fair200_quick3h_20260509
- repo/coursework/new_datasets/alloy/mace_ablation_normal_ew10_ew50_20260509
- repo/coursework/new_datasets/alloy/mace_ablation_normal_protocols_20260509
- repo/coursework/new_datasets/alloy/mace_ablation_20260509
- for_gpt selected summaries

How to use for presentation update:
1. Start from metrics/final_metrics_wide.csv for final tables.
2. Use metrics/alloy_mace_ablation_table.md for the alloy MACE ablation slide.
3. Use metrics/water_mtp_table.md for the H2O MTP-16 vs MTP-20 slide.
4. Use FINAL_CLAIMS_AND_CAVEATS.md to keep slide claims safe.
5. Use source_manifest.tsv to locate copied source files and logs.

Key final recommendations:
- H2O final: show old MTP-16 and clean MTP-20 separately.
- Alloy final MACE: use MACE-EW50 as the best energy-weighted MACE result, with the caveat that default MACE was worse.
- Do not use quick/preempted partial runs as final unless eval_train/eval_valid JSON exists.
