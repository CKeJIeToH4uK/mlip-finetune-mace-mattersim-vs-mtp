# Журнал русификации Markdown

## Цель

Этот pass убирает русско-английский суржик из обычной прозы Markdown-документов. Правки не меняют финальные числа, source-of-truth иерархию, пути, команды, названия моделей, метрики, единицы измерения и split labels.

## Измененные Markdown-файлы

- `README.md`
- `PROJECT_STRUCTURE.md`
- `REPRODUCIBILITY.md`
- `archive/excluded_heavy_manifest.md`
- `archive/old_experiments_manifest.md`
- `configs/README.md`
- `docs/datasets_and_splits.md`
- `docs/experiment_protocol.md`
- `docs/limitations.md`
- `docs/models.md`
- `docs/problem_statement.md`
- `docs/provenance.md`
- `docs/results_summary.md`
- `provenance/source_manifests/README.md`
- `provenance/source_mirror/README.md`
- `provenance/protocols/presentation_handoff/protocols_eval_addendum_20260510/README_ADDENDUM.md`
- `scripts/README.md`
- `src/mlip_benchmark/README.md`

## Основные замены

| Было | Стало | Причина |
|---|---|---|
| `Curated Coursework Repository` | `Проверяемый репозиторий курсового проекта` | Русский заголовок лучше соответствует языку документа. |
| `provenance-артефакты` | `материалы происхождения результатов` | Убирает гибридную формулировку без изменения смысла. |
| `clean repo` | `очищенный репозиторий` / `этот репозиторий` | Английская фраза не нужна в обычной прозе. |
| `energy-weighted протокол` | `протокол с увеличенным весом ошибки энергии` | Сохраняет технический смысл и делает текст естественнее. |
| `handoff-таблицы` | `сопроводительные таблицы` | Оставляет `handoff_tables` только в путях. |
| `preview/backup материалы` | `материалы предпросмотра и резервные материалы` | Убирает лишний английский из описания папки. |
| `manifest-файлы` | `манифесты` / `файлы-манифесты` | Унифицирует русскую prose-терминологию. |
| `caches` | `служебные кэши` | Русская форма точнее для списка исключений. |
| `eval snapshots` | `исходные файлы оценки` | Убирает английский scaffold из методологического текста. |
| `presentation handoffs` | `сопроводительные материалы презентации` | Делает описание архивных материалов нейтральным. |
| `MD-стабильность` | `стабильность MD-траекторий` | Сохраняет доменный термин и улучшает читаемость. |

## Сохраненные guardrails

- Пути и команды не переводились.
- Названия моделей `MTP`, `MACE`, `MatterSim`, `MACE-EW50` и `MACE default` не менялись.
- Метрики и единицы `MAE`, `RMSE`, `meV/atom`, `meV/Å`, `CSV`, `JSON` не менялись.
- Split labels `train`, `valid`, `validation` и `held-out validation` сохранялись там, где они являются точными обозначениями.
- `organic-датасет` оставлен как стабильное обозначение проекта.
- `archive/old_contexts/**`, `results/*.csv` и `provenance/raw_eval_refs/*.json` не редактировались.
- Точные ссылки `provenance/handoff_tables/final_metrics_long.csv` и `provenance/handoff_tables/final_metrics_wide.csv` сохранены в `docs/results_summary.md`.

## Проверки

После правок должны быть выполнены:

```bash
git diff --check
git diff --name-only | grep -E '(^results/.*\.csv$|^provenance/raw_eval_refs/.*\.json$|^archive/old_contexts/)' || true
git grep -n "provenance/handoff_tables/final_metrics_long.csv" -- '*.md' || true
git grep -n "provenance/handoff_tables/final_metrics_wide.csv" -- '*.md' || true
python scripts/validate_manifests.py
python scripts/validate_results.py
```

Итоги конкретного запуска фиксируются в финальном сообщении к этому pass-у.
