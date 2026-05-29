# Reproducibility Scope

Этот репозиторий позволяет проверить согласованность финальных таблиц, проследить происхождение результатов, просмотреть код агрегации и оценки, а также подготовить материалы для отчета. Полное переобучение моделей с нуля из этого репозитория не поддерживается.

## Что включено

- verified metrics CSV;
- backup/appendix/sanity таблицы;
- small eval JSON/CSV snapshots;
- summaries, log snippets, slurm scripts;
- полезные Python/shell/sbatch scripts;
- фигуры и презентационные материалы;
- manifests and checksums.

## Что не включено физически

- raw datasets;
- checkpoints and model weights;
- heavy archives;
- build outputs and local binaries;
- nested repositories and service caches.

Эти активы перечислены в `provenance/source_manifests/excluded_heavy_manifest.csv` или `provenance/source_manifests/archive_external_manifest.csv`.

## Practical Checks

```bash
python scripts/validate_manifests.py
python scripts/validate_results.py
```

Ожидаемый уровень воспроизводимости ограничен проверкой согласованности включенных таблиц, скриптов и provenance-материалов. Полная процедура обучения требует внешних тяжелых данных и артефактов, которые намеренно не входят в clean repo.

## Manifest Self-Reference Policy

`included_manifest.csv`, `excluded_heavy_manifest.csv`, and `archive_external_manifest.csv` are control files. They may be absent from `included_manifest.csv` to avoid circular manifest semantics. `checksums.sha256` intentionally excludes itself; it covers copied/generated artifacts and manifest CSVs.

Historical absolute paths are allowed only in `provenance/`, manifests, logs, and raw eval refs as source history. Runnable/root docs and curated helper modules should not depend on local absolute paths.
