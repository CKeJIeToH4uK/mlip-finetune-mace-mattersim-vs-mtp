# Reproducibility Scope

Этот репозиторий позволяет проверить согласованность финальных таблиц, проследить происхождение результатов, просмотреть код агрегации и оценки, а также подготовить материалы для отчета. Полное переобучение моделей с нуля из этого репозитория не поддерживается.

## Что включено

- проверенные CSV-файлы с метриками;
- таблицы для приложения, дополнительные проверки и sanity-check материалы;
- небольшие JSON/CSV-файлы с результатами оценки;
- сводки, фрагменты логов и slurm-скрипты;
- полезные Python- и sbatch-скрипты;
- графики и презентационные материалы;
- manifests и checksums.

## Что не включено физически

- исходные датасеты;
- checkpoints и веса моделей;
- тяжелые архивы;
- build outputs и локальные бинарные файлы;
- вложенные репозитории и служебные caches.

Эти активы перечислены в `provenance/source_manifests/excluded_heavy_manifest.csv` или `provenance/source_manifests/archive_external_manifest.csv`.

## Practical Checks

```bash
python scripts/validate_manifests.py
python scripts/validate_results.py
```

Ожидаемый уровень воспроизводимости ограничен проверкой согласованности включенных таблиц, скриптов и материалов происхождения результатов. Полная процедура обучения требует внешних тяжелых данных и артефактов, которые намеренно не входят в clean repo.

## Manifest Self-Reference Policy

`included_manifest.csv`, `excluded_heavy_manifest.csv` и `archive_external_manifest.csv` являются control files. Они могут отсутствовать в `included_manifest.csv`, чтобы не создавать циклические записи. `checksums.sha256` намеренно исключает сам себя; он покрывает скопированные и сгенерированные материалы, а также manifest CSVs.

Исторические absolute paths допустимы только в `provenance/`, manifests, logs и raw eval refs как часть истории источников. Root docs и curated helper modules не должны зависеть от локальных absolute paths.
