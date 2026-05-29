# Структура curated repo

`coursework_clean/` собран как полный, но отфильтрованный исследовательский репозиторий. Он не является маленьким пакетом сдачи: здесь сохранены результаты, provenance, полезный код, протоколы, графики и архивный контекст.

## Корень

- `README.md`: назначение и быстрый старт.
- `REPRODUCIBILITY.md`: что можно проверить локально и какие активы исключены.
- `requirements.txt`: окружение для review/evaluation/table/figure scripts, без обещания полного переобучения.

## Основные папки

- `docs/`: постановка задачи, датасеты, модели, метрики, результаты, ограничения и provenance.
- `results/verified_metrics/`: system-specific verified CSV and derived annotated status copies.
- `results/appendix_tables/`: backup/appendix таблицы и расширенные протоколы.
- `results/sanity_checks/`: sanity-check таблицы, включая MTP ensemble для organic 300K.
- `results/figures/` и `report_assets/figures/`: отобранные графики для просмотра и будущего отчета.
- `provenance/handoff_tables/`: handoff/support tables copied from final context; not complete final source-of-truth.
- `provenance/source_mirror/`: historical source mirror for provenance only, not runnable package surface.
- `provenance/`: summaries, log snippets, slurm scripts, raw eval snapshots, manifests and checksums.
- `src/mlip_benchmark/`: легкие curated helpers в `analysis/`, `evaluation`, `plotting`, `utils`.
- `scripts/`: проверки clean repo и легкие helper scripts.
- `presentation_archive/`: финальная презентация и выбранные preview/backup материалы.
- `archive/`: старый контекст и исключенные ветки как история, не numeric authority.
