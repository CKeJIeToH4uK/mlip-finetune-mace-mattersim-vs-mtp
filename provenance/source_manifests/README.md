# Source Manifests

CSV-файлы в этой папке фиксируют provenance для clean repo.

- `included_manifest.csv`: скопированные и сгенерированные артефакты clean repo, кроме управляющих файлов, которые создавали бы циклические manifest-записи.
- `excluded_heavy_manifest.csv`: исходные датасеты, чекпоинты, веса моделей, результаты сборки, бинарные файлы и другие тяжелые артефакты, намеренно не включенные физически.
- `archive_external_manifest.csv`: старые контексты, внешние зоны, учебные папки, архивы и reference-only материалы, которые не копировались целиком.

## Self-Reference Exceptions

Manifest-файлы могут отсутствовать в `included_manifest.csv`; это сделано, чтобы избежать самоссылочных строк. `checksums.sha256` намеренно исключает сам себя и покрывает остальные manifest-файлы вместе с обычными скопированными или сгенерированными артефактами.

## Canonical Schema

Текущие CSV-заголовки являются каноническими для clean repo. Ранние поля из build plan, такие как `kind`, `archive_status` или `replacement_reference`, представлены текущими колонками `category`, `artifact_type`, `possible_relevance`, `reason_not_copied` и `notes`, где это применимо.
