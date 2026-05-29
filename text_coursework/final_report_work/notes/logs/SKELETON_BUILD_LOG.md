# Skeleton build log

Дата: 2026-05-29

## Созданные директории

- `text_coursework/final_report_work/`
- `text_coursework/final_report_work/sections/`
- `text_coursework/final_report_work/figures/`
- `text_coursework/final_report_work/tables/`
- `text_coursework/final_report_work/notes/`
- `text_coursework/final_report_work/notes/logs/`

## Созданные файлы

- `main.tex`
- `ref.bib`
- `sections/00_abstract.tex`
- `sections/01_introduction.tex`
- `sections/02_problem_metrics.tex`
- `sections/03_methods_literature.tex`
- `sections/04_experiment_protocol.tex`
- `sections/05_results_discussion.tex`
- `sections/06_limitations.tex`
- `sections/07_conclusion.tex`
- `sections/appendix.tex`
- `notes/REPORT_STRUCTURE.md`
- `notes/SOURCE_OF_TRUTH_RULES.md`
- `notes/TODO.md`
- `notes/logs/SKELETON_BUILD_LOG.md`
- `figures/.gitkeep`
- `tables/.gitkeep`

## Просмотренные существующие источники и шаблоны

- `README.md`: назначение clean repo, основные системы, модели и правила источников результатов.
- `PROJECT_STRUCTURE.md`: карта директорий clean repo.
- `docs/problem_statement.md`: постановка задачи и список основных систем.
- `docs/metrics.md`: метрики, единицы и ссылка на `../text_coursework/RESULTS_SOURCE_OF_TRUTH.md`.
- `docs/models.md`: различение `MACE default` и `MACE-EW50`.
- `docs/results_summary.md`: правила использования verified CSV и запрет подмены source-of-truth handoff-таблицами.
- `provenance/handoff_tables/*`: найдено как вспомогательный источник происхождения, не как главный источник чисел.
- Поиск `*.tex` и `*.bib` в clean repo: готовых LaTeX/BibTeX шаблонов не найдено.
- Локальный `/Users/bulat/HSE/LinRegProject/mlip-4/README.md`: использован как ориентир для заготовки ссылки на MLIP-4.

## Просмотренные внешние/документационные источники для `ref.bib`

- Context7: `/websites/mace-docs_readthedocs_io_en`, разделы fine-tuning MACE.
- Context7: `/microsoft/mattersim`, README и fine-tuning MatterSim.
- arXiv: MatterSim, `arXiv:2405.04967`.
- arXiv: MACE, `arXiv:2206.07697`.
- Nature Computational Science: M3GNet, DOI `10.1038/s43588-022-00349-3`.
- GitLab: `https://gitlab.com/ashapeev/mlip-4`.

## Ограничения при создании каркаса

- Commit не выполнялся.
- В итоговом состоянии новые или измененные файлы вне `text_coursework/final_report_work/` не оставлены.
- Тяжелые файлы, датасеты, веса, чекпоинты и архивы не добавлялись.
- Финальные численные результаты в секции отчета не добавлялись.

## Проверка сборки

- Выполнена сборка `main.tex` через LaTeX-плагин командой `latexmk -xelatex` во временный каталог `/tmp/final_report_work_latex_build`.
- Сборка завершилась с кодом `0`; PDF был создан во временном каталоге.
- Build-артефакты в `text_coursework/final_report_work/` не добавлялись.

## Review-fix pass 2026-05-29

- Добавлен `notes/CITATION_AND_ANTI_PLAGIARISM_RULES.md`.
- В `main.tex` тема титульного листа заменена на утвержденную формулировку.
- Поля изменены на `left=25mm,right=10mm,top=20mm,bottom=20mm`.
- Основной шрифт заменен на `Times New Roman`; моноширинный шрифт установлен как `Courier New`.
- `\nocite{*}` убран из активного LaTeX-кода и заменен комментарием о явном цитировании источников.
- В `notes/TODO.md` добавлен финальный citation-check.
- После правок выполнена свежая сборка `main.tex` через LaTeX-плагин командой `latexmk -xelatex` во временный каталог `/tmp/final_report_work_latex_build`.
- Сборка завершилась с кодом `0`; PDF был создан во временном каталоге.
- В логе сборки есть ожидаемое предупреждение `Empty thebibliography`, потому что `\nocite{*}` убран, а явные `\cite{...}` еще не добавлены в placeholder-текст.
- Commit в рамках этого review-fix pass не выполнялся.

## Повторная проверка по запросу 2026-05-29

- Повторно выполнена сборка `main.tex` через LaTeX-плагин командой `latexmk -xelatex` во временный каталог `/tmp/final_report_work_latex_build`.
- Сборка завершилась с кодом `0`; PDF создан во временном каталоге.
- Предупреждение `Empty thebibliography` остается ожидаемым до добавления явных `\cite{...}` в текст.
- Build-артефакты в `text_coursework/final_report_work/` не добавлялись.
- Commit не выполнялся.
