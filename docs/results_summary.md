# Results Summary

Этот документ кратко фиксирует, где лежат финальные результаты. Числа берутся из `results/verified_metrics/` and supporting CSV files; текст отчета должен ссылаться на эти таблицы, а не на старые handoff materials.

## Main Result Tables

- `results/verified_metrics/organic_metrics_verified_20260511.csv`: organic-датасет, cross-temperature rows.
- `results/verified_metrics/h2o_metrics_verified_20260511.csv`: H2O held-out validation rows and separated train support rows where present.
- `results/verified_metrics/monbtavw_metrics_verified_20260511.csv`: MoNbTaVW held-out validation rows, with MTP audit caveat handled separately.
- `results/verified_metrics/final_metrics_long.csv` and `results/verified_metrics/final_metrics_wide.csv`: consolidated final tables.

## Sanity Checks

- `results/sanity_checks/ensemble_aggregates_verified_20260511.csv`: MTP ensemble sanity check for organic 300K only.

## Claim Discipline

Allowed claims are metric-specific and table-backed. Broad model-family generalizations, performance-cost claims, and long-trajectory stability claims are outside the clean repo source-of-truth.
