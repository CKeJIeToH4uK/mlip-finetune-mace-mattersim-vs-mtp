# MTP ENSEMBLE AUDIT 2026-05-11

## 1. Scope

This audit documents available ensemble evidence only. It does not change slides, plots, training/evaluation outputs, raw datasets, checkpoints, or model weights.

Searched:

- `PRESENTATION/00_inbox/`
- `PRESENTATION/01_unpacked/`
- `PRESENTATION/03_content/`
- `PRESENTATION/04_assets/`
- nested archives in `PRESENTATION/00_inbox/`
- `repo/coursework/`

Main sources inspected:

- `PRESENTATION/00_inbox/presentation_full_context.zip`
- `PRESENTATION/01_unpacked/ensemble_audit_20260511/presentation_full_context/`
- `repo/coursework/mtp_runs/`
- `repo/coursework/cross_temp_eval/results/mtp/`
- `FINAL_NEW_CHAT_CONTEXT_20260511/05_reports_metrics/ENSEMBLE_AUDIT_REPORT_20260511.md`
- `PRESENTATION/03_content/ensemble_raw_runs_index_20260511.csv`
- `PRESENTATION/03_content/ensemble_aggregates_verified_20260511.csv`

## 2. Short Answer

For organic cross-temperature test evaluation, 5-run MTP ensembles were **not** found.

| Level | 5 training runs found? | 5 cross-temperature test runs found? | Test temperatures found | Decision |
|---|---:|---:|---|---|
| MTP-16 | yes, train/valid 300K summaries | no, only `run-1` | 300K, 600K, 1200K | cannot compute test mean ± std |
| MTP-20 | yes, train/valid 300K summaries | no, only `run-1` | 300K, 600K, 1200K | cannot compute test mean ± std |

The available cross-temperature JSON files explicitly point to:

- `level16_run1/mtp16_trained.json`
- `level20_run1/mtp20_trained.json`

No `level16_run2`--`level16_run5` or `level20_run2`--`level20_run5` cross-temperature test JSON files were found.

## 3. Test Metrics Found

All required test metrics exist for `run-1` only:

- Energy MAE
- Energy RMSE
- Forces MAE
- Forces RMSE

Units:

- source energy unit: `eV/atom`, converted to `meV/atom`;
- source force unit: `meV/A`, reported as `meV/Å`.

Created test-run CSV:

- `PRESENTATION/03_content/organic_mtp_ensemble_runs_20260511.csv`

Created test aggregate CSV:

- `PRESENTATION/03_content/organic_mtp_ensemble_aggregates_20260511.csv`

The aggregate CSV has `n_runs=1` for each level and test temperature. Means equal the single available run; std columns are intentionally blank because std is not defined for one run.

## 4. Cross-Temperature Test Runs

| level | run_id | test_temperature | Energy MAE, meV/atom | Energy RMSE, meV/atom | Forces MAE, meV/Å | Forces RMSE, meV/Å | source |
|---|---|---:|---:|---:|---:|---:|---|
| MTP-16 | run-1 | 300K | 1.965594 | 2.578954 | 172.175900 | 251.039200 | `repo/coursework/cross_temp_eval/results/mtp/test_300K_mtp16.json` |
| MTP-16 | run-1 | 600K | 4.677083 | 6.495860 | 256.605100 | 375.815700 | `repo/coursework/cross_temp_eval/results/mtp/test_600K_mtp16.json` |
| MTP-16 | run-1 | 1200K | 14.777900 | 20.442030 | 441.936600 | 748.242900 | `repo/coursework/cross_temp_eval/results/mtp/test_1200K_mtp16.json` |
| MTP-20 | run-1 | 300K | 1.632113 | 2.099471 | 140.196000 | 205.931700 | `repo/coursework/cross_temp_eval/results/mtp/test_300K_mtp20.json` |
| MTP-20 | run-1 | 600K | 3.725958 | 5.030732 | 218.808800 | 331.139900 | `repo/coursework/cross_temp_eval/results/mtp/test_600K_mtp20.json` |
| MTP-20 | run-1 | 1200K | 10.244110 | 13.463010 | 402.400300 | 661.379600 | `repo/coursework/cross_temp_eval/results/mtp/test_1200K_mtp20.json` |

The same six test rows are also present inside:

- `PRESENTATION/00_inbox/presentation_full_context.zip::repo/coursework/cross_temp_eval/results/mtp/`
- `PRESENTATION/00_inbox/presentation_full_context.zip::19.03.26/cross_temp_eval_300_600_1200K_current/results/mtp/`

The dated `19.03.26` copy is a duplicate result snapshot, not additional runs.

## 5. Repeated MTP Runs Found

Five repeated MTP jobs per level were found in:

- `PRESENTATION/00_inbox/presentation_full_context.zip::26.02.26/mtp_errors_summary.csv`

These rows are final train/validation 300K summaries, not cross-temperature test evaluations.

### MTP-16 repeated train/valid 300K rows

| run_id | split | Energy MAE, meV/atom | Energy RMSE, meV/atom | Forces MAE, meV/Å | Forces RMSE, meV/Å | source log |
|---|---|---:|---:|---:|---:|---|
| job_3633630 | train_300K | 2.007635 | 2.490290 | 179.9590 | 253.2214 | `26.02.26/logs_16/mtp_train_3633630.out` |
| job_3633640 | train_300K | 1.357125 | 1.718205 | 132.1461 | 196.3622 | `26.02.26/logs_16/mtp_train_3633640.out` |
| job_3633641 | train_300K | 1.492311 | 1.882204 | 150.6989 | 216.6090 | `26.02.26/logs_16/mtp_train_3633641.out` |
| job_3633642 | train_300K | 1.980078 | 2.601657 | 227.8103 | 348.7249 | `26.02.26/logs_16/mtp_train_3633642.out` |
| job_3633645 | train_300K | 1.731441 | 2.187501 | 182.0090 | 274.4733 | `26.02.26/logs_16/mtp_train_3633645.out` |
| job_3633630 | valid_300K | 2.351885 | 3.057517 | 184.5034 | 259.6372 | `26.02.26/logs_16/mtp_train_3633630.out` |
| job_3633640 | valid_300K | 1.713751 | 2.184240 | 134.2881 | 199.7519 | `26.02.26/logs_16/mtp_train_3633640.out` |
| job_3633641 | valid_300K | 1.935368 | 2.499776 | 154.9826 | 222.7721 | `26.02.26/logs_16/mtp_train_3633641.out` |
| job_3633642 | valid_300K | 2.632334 | 3.433330 | 232.7791 | 357.6304 | `26.02.26/logs_16/mtp_train_3633642.out` |
| job_3633645 | valid_300K | 2.167742 | 2.757885 | 187.1374 | 285.2193 | `26.02.26/logs_16/mtp_train_3633645.out` |

### MTP-20 repeated train/valid 300K rows

| run_id | split | Energy MAE, meV/atom | Energy RMSE, meV/atom | Forces MAE, meV/Å | Forces RMSE, meV/Å | source log |
|---|---|---:|---:|---:|---:|---|
| job_3633647 | train_300K | 1.175476 | 1.499195 | 121.5734 | 172.8129 | `26.02.26/logs_20/mtp_train_3633647.out` |
| job_3633648 | train_300K | 1.558755 | 1.952223 | 162.2719 | 232.0197 | `26.02.26/logs_20/mtp_train_3633648.out` |
| job_3633653 | train_300K | 1.611034 | 2.009893 | 173.8977 | 255.8913 | `26.02.26/logs_20/mtp_train_3633653.out` |
| job_3633656 | train_300K | 1.343398 | 1.701695 | 145.9906 | 209.4302 | `26.02.26/logs_20/mtp_train_3633656.out` |
| job_3633657 | train_300K | 1.273207 | 1.602894 | 132.8052 | 190.0474 | `26.02.26/logs_20/mtp_train_3633657.out` |
| job_3633647 | valid_300K | 1.527191 | 2.021561 | 124.8597 | 178.2621 | `26.02.26/logs_20/mtp_train_3633647.out` |
| job_3633648 | valid_300K | 2.135196 | 2.788955 | 167.7037 | 245.9572 | `26.02.26/logs_20/mtp_train_3633648.out` |
| job_3633653 | valid_300K | 2.195036 | 2.859348 | 179.5148 | 264.3391 | `26.02.26/logs_20/mtp_train_3633653.out` |
| job_3633656 | valid_300K | 1.756881 | 2.255757 | 149.8847 | 215.7340 | `26.02.26/logs_20/mtp_train_3633656.out` |
| job_3633657 | valid_300K | 1.752638 | 2.271213 | 138.1769 | 197.9895 | `26.02.26/logs_20/mtp_train_3633657.out` |

Units in `mtp_errors_summary.csv`:

- source energy per atom is `eV/atom`, converted to `meV/atom`;
- source forces are `eV/A`, converted to `meV/Å`.

## 6. Mean ± Std Eligibility

| Scope | MTP-16 n | MTP-20 n | Can compute mean ± std? | Notes |
|---|---:|---:|---|---|
| test_300K | 1 | 1 | no | only `run-1` cross-temperature JSON exists |
| test_600K | 1 | 1 | no | only `run-1` cross-temperature JSON exists |
| test_1200K | 1 | 1 | no | only `run-1` cross-temperature JSON exists |
| train_300K | 5 | 5 | yes | final train summaries only, not held-out cross-temperature tests |
| valid_300K | 5 | 5 | yes | validation summaries only, not 600K/1200K transfer tests |

Existing verified train/valid aggregates from `PRESENTATION/03_content/ensemble_aggregates_verified_20260511.csv`:

| level | split | n_runs | Energy MAE mean ± std | Energy RMSE mean ± std | Forces MAE mean ± std | Forces RMSE mean ± std |
|---|---|---:|---:|---:|---:|---:|
| MTP-16 | train_300K | 5 | 1.713718 ± 0.288890 | 2.175971 ± 0.379469 | 174.524660 ± 36.361092 | 257.878160 ± 59.240128 |
| MTP-16 | valid_300K | 5 | 2.160216 ± 0.356923 | 2.786550 ± 0.484145 | 178.738120 ± 37.297262 | 265.002180 ± 61.356501 |
| MTP-20 | train_300K | 5 | 1.392374 ± 0.186507 | 1.753180 ± 0.220944 | 147.307760 ± 21.244216 | 212.040300 ± 32.982479 |
| MTP-20 | valid_300K | 5 | 1.873388 ± 0.282846 | 2.439367 ± 0.365768 | 152.027960 ± 21.998949 | 220.456380 ± 34.940677 |

These aggregates must not be used as substitutes for 300K/600K/1200K cross-temperature test mean ± std.

## 7. Missing Items

For a complete organic MTP test ensemble, the following are missing:

- MTP-16 cross-temperature test metrics for `run-2`, `run-3`, `run-4`, `run-5` at 300K;
- MTP-16 cross-temperature test metrics for `run-2`, `run-3`, `run-4`, `run-5` at 600K;
- MTP-16 cross-temperature test metrics for `run-2`, `run-3`, `run-4`, `run-5` at 1200K;
- MTP-20 cross-temperature test metrics for `run-2`, `run-3`, `run-4`, `run-5` at 300K;
- MTP-20 cross-temperature test metrics for `run-2`, `run-3`, `run-4`, `run-5` at 600K;
- MTP-20 cross-temperature test metrics for `run-2`, `run-3`, `run-4`, `run-5` at 1200K.

Also not found in `repo/coursework/mtp_runs/`:

- `level16_run2/` through `level16_run5/`;
- `level20_run2/` through `level20_run5/`.

## 8. Audit Decision

The requirement for an ensemble of 5 MTP potentials at levels 16 and 20 is only partially represented in the available materials. Five repeated MTP training/validation jobs exist per level for organic 300K, but the organic cross-temperature result block has only one tested potential per level at 300K/600K/1200K.

For this reason, the existing organic result slides should remain single-run MTP lines unless new verified cross-temperature evaluations for the other four runs per level are added.
