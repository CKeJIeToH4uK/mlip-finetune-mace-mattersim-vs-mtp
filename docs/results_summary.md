# Сводка результатов

Этот документ показывает, где в clean repo находятся материалы с результатами. Он не заменяет внешний рабочий документ `text_coursework/RESULTS_SOURCE_OF_TRUTH.md`, который остается основным источником финальных чисел и допустимых claims.

## Источник финальных чисел

Для текста отчета использовать:

1. внешний документ `text_coursework/RESULTS_SOURCE_OF_TRUTH.md`;
2. system-specific verified CSV-файлы из этого репозитория:
   - `results/verified_metrics/organic_metrics_verified_20260511.csv`;
   - `results/verified_metrics/h2o_metrics_verified_20260511.csv`;
   - `results/verified_metrics/monbtavw_metrics_verified_20260511.csv`;
   - `results/verified_metrics/monbtavw_metrics_verified_20260511_annotated.csv` — только для row-level `metric_status`.

## Handoff/Support Tables

Таблицы `final_metrics_long.csv` и `final_metrics_wide.csv` в `provenance/handoff_tables/` являются вспомогательными handoff-таблицами. Их можно использовать для сверки provenance, но они не должны переопределять system-specific verified CSV и `RESULTS_SOURCE_OF_TRUTH.md`.

## Sanity Checks

- `results/sanity_checks/ensemble_aggregates_verified_20260511.csv`: MTP ensemble sanity check только для organic 300K.

## Claim Discipline

Выводы в отчете должны формулироваться по конкретной системе, разбиению и метрике. Обобщения вида «универсальные модели всегда лучше», утверждения о вычислительной стоимости и выводы о долгой MD-стабильности не подтверждаются текущими verified таблицами.
