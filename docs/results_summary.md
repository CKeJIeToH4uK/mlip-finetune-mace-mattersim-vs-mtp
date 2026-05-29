# Сводка результатов

Этот документ показывает, где в репозитории находятся материалы с результатами. Он не заменяет внешний рабочий документ `../text_coursework/RESULTS_SOURCE_OF_TRUTH.md`, который намеренно не входит в очищенный репозиторий и остается основным источником финальных чисел и допустимых выводов.

## Источник финальных чисел

Для текста отчета использовать:

1. внешний документ `../text_coursework/RESULTS_SOURCE_OF_TRUTH.md`;
2. проверенные CSV-файлы по отдельным системам из этого репозитория:
   - `results/verified_metrics/organic_metrics_verified_20260511.csv`;
   - `results/verified_metrics/h2o_metrics_verified_20260511.csv`;
   - `results/verified_metrics/monbtavw_metrics_verified_20260511.csv`;
   - `results/verified_metrics/monbtavw_metrics_verified_20260511_annotated.csv` — только для статусов строк `metric_status`.

## Вспомогательные таблицы

`provenance/handoff_tables/final_metrics_long.csv` и `provenance/handoff_tables/final_metrics_wide.csv` являются вспомогательными сопроводительными таблицами. Их можно использовать для сверки происхождения результатов, но они не должны переопределять проверенные CSV по отдельным системам и `RESULTS_SOURCE_OF_TRUTH.md`.

## Дополнительные проверки

- `results/sanity_checks/ensemble_aggregates_verified_20260511.csv`: дополнительная проверка MTP ensemble только для organic 300K.

## Правила формулирования выводов

Выводы в отчете должны формулироваться по конкретной системе, разбиению и метрике. Текущие проверенные таблицы не подтверждают широких обобщений о классе моделей, выводов о вычислительной стоимости или утверждений о долгой стабильности MD-траекторий.
