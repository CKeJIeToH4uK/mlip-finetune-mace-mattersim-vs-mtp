# Reproducibility Scope

Этот clean repo поддерживает проверку финальных таблиц, просмотр source chains, ревью кода агрегации/evaluation и подготовку отчета. Он не обещает полное переобучение с нуля.

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

Ожидаемый уровень воспроизводимости: проверка согласованности curated artifacts и provenance. Полный training pipeline требует внешних heavy/raw assets, которые не входят в этот repo.

## Manifest Self-Reference Policy

`included_manifest.csv`, `excluded_heavy_manifest.csv`, and `archive_external_manifest.csv` are control files. They may be absent from `included_manifest.csv` to avoid circular manifest semantics. `checksums.sha256` intentionally excludes itself; it covers copied/generated artifacts and manifest CSVs.

Historical absolute paths are allowed only in `provenance/`, manifests, logs, and raw eval refs as source history. Runnable/root docs and curated helper modules should not depend on local absolute paths.
