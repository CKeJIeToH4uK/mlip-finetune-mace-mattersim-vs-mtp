# Структура curated repo

`coursework_clean/` — это полная, но отфильтрованная версия исследовательского репозитория. Она предназначена не только для сдачи итогового отчета, но и для просмотра результатов, проверки provenance, анализа кода, протоколов экспериментов, графиков и архивного контекста.

## Корень

- `README.md` — назначение репозитория и быстрый старт.
- `REPRODUCIBILITY.md` — что можно проверить локально и какие активы намеренно исключены.
- `requirements.txt` — окружение для review, evaluation, table и figure scripts; файл не обещает полного переобучения моделей.

## Основные папки

- `docs/` — постановка задачи, описание датасетов, моделей, метрик, результатов, ограничений и provenance.
- `results/verified_metrics/` — проверенные CSV-файлы с метриками по отдельным системам и производные аннотированные таблицы.
- `results/appendix_tables/` — дополнительные таблицы для приложения и расширенные протокольные результаты.
- `results/sanity_checks/` — sanity-check таблицы, включая MTP ensemble для organic 300K.
- `results/figures/` и `report_assets/figures/` — отобранные графики для просмотра и будущего отчета.
- `provenance/handoff_tables/` — вспомогательные handoff-таблицы; они не являются полным источником финальных результатов.
- `provenance/source_mirror/` — историческое зеркало исходных скриптов, сохраненное только для provenance.
- `provenance/` — summaries, log snippets, slurm scripts, raw eval snapshots, manifests и checksums.
- `src/mlip_benchmark/` — легкие curated helpers в `analysis/`, `evaluation`, `plotting` и `utils`.
- `scripts/` — проверки clean repo и легкие helper scripts.
- `presentation_archive/` — финальная презентация и выбранные preview/backup материалы.
- `archive/` — старый контекст и исключенные ветки как история, не numeric authority.
