# Curated Coursework Repository

Этот репозиторий содержит очищенную и структурированную версию материалов курсового проекта. В него включены финальные проверенные метрики, вспомогательные таблицы, материалы для отслеживания происхождения результатов, отобранные скрипты анализа, графики, презентационные материалы и архивный контекст, необходимый для проверки проведенных экспериментов.

Крупные исходные данные, веса моделей, checkpoints, тяжелые архивы, локальные бинарные файлы, вложенные репозитории и build outputs не включены физически. Их расположение и роль описаны в `provenance/source_manifests/`.

Основным источником финальных численных результатов для отчета является внешний рабочий документ `text_coursework/RESULTS_SOURCE_OF_TRUTH.md`. Внутри этого репозитория ему соответствуют system-specific verified CSV-файлы в `results/verified_metrics/`: organic-датасет, H2O и MoNbTaVW. Таблицы из `provenance/handoff_tables/` используются только как вспомогательные материалы для сверки происхождения результатов и не являются полным source-of-truth.

Основные системы и модели: organic-датасет, H2O, MoNbTaVW; MTP, MACE, MatterSim и energy-weighted MACE protocol rows для MoNbTaVW.

См. также `PROJECT_STRUCTURE.md` для навигации по репозиторию и `REPRODUCIBILITY.md` для описания того, что можно проверить локально, а какие активы намеренно исключены.

## Quick Map

- `docs/` — краткие методологические описания: постановка задачи, данные, протокол экспериментов, модели, метрики, результаты, происхождение результатов и ограничения.
- `results/` — проверенные таблицы метрик, вспомогательные таблицы, sanity checks и отобранные графики.
- `provenance/` — материалы происхождения результатов: handoff tables, source mirror, log snippets, slurm scripts, manifests, checksums и raw eval refs.
- `src/mlip_benchmark/` — легкие curated helper modules для анализа, проверки результатов и построения таблиц/графиков.
- `scripts/` — validation scripts и вспомогательные команды для работы с clean repo.
- `presentation_archive/` — финальная презентация и выбранные preview/backup материалы.
- `archive/` — старые контексты и исключенные ветки, не являющиеся источником финальных чисел.

## Validation

Run:

```bash
python scripts/validate_manifests.py
python scripts/validate_results.py
```

Эти скрипты проверяют покрытие manifests, исключенные artifacts, наличие обязательных metric files, терминологические guardrails и согласованность checksums для скопированных материалов.
