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

## Title page update 2026-05-30

- В `main.tex` заменен только блок `\begin{titlepage} ... \end{titlepage}` на титульный лист по образцу КТ1.
- В преамбулу `main.tex` добавлен только пакет `tabularx`, необходимый для титульного листа.
- Старые разделы, аннотация, введение, рисунки и библиография из КТ1 не переносились.
- Выполнена сборка из `text_coursework/final_report_work/` командой `latexmk -xelatex main.tex`.
- Сборка завершилась с кодом `0`; PDF создан.
- Нефатальные предупреждения: `Empty thebibliography` ожидаемо до добавления явных `\cite{...}`; `Underfull \hbox` относится к верстке титульного листа.
- Commit не выполнялся.

## Build config update 2026-05-30

- В корневой `.gitignore` добавлены недостающие LaTeX build-артефакты для `text_coursework/final_report_work/`: `.bbl`, `.blg`, `.pdf`, `.synctex.gz`, `.xdv`.
- Добавлен `text_coursework/final_report_work/.latexmkrc`, чтобы обычный запуск `latexmk main.tex` использовал XeLaTeX.
- В `.latexmkrc` выставлен режим BibTeX cleanup, при котором `latexmk -C main.tex` удаляет сгенерированный `main.bbl`.
- Причина предыдущей ошибки сборки: запуск `latexmk main.tex` без `.latexmkrc` выбирал стандартный `latex`/pdfTeX flow, а текущий `main.tex` использует `fontspec`, которому нужен XeLaTeX или LuaLaTeX.
- Выполнена свежая проверка `latexmk -g main.tex` из `text_coursework/final_report_work/`; сборка завершилась с кодом `0`, PDF был создан.
- Выполнена проверка через LaTeX-плагин: `compile_latex.py main.tex --compiler texlive --engine xelatex`; сборка завершилась с кодом `0`.
- После проверки локальные build-артефакты удалены командой `latexmk -C main.tex`; оставшийся `main.bbl` удален как сгенерированный BibTeX-артефакт.
- Нефатальные предупреждения остаются ожидаемыми для каркаса: `Empty thebibliography` до добавления явных `\cite{...}` и `Underfull \hbox` на титульном листе.

## PDF tracking update 2026-05-30

- По запросу пользователя `text_coursework/final_report_work/main.pdf` оставлен как отслеживаемый артефакт отчета.
- Из `.gitignore` удалено правило `text_coursework/final_report_work/*.pdf`.
- Остальные побочные файлы сборки LaTeX остаются игнорируемыми.

## Introduction text update 2026-05-30

- В `sections/01_introduction.tex` заменены placeholder-абзацы на предоставленный пользователем текст раздела `Введение`.
- Содержательный текст пользователя не изменялся.
- `ref.bib` не изменялся: все citation keys из вставленного текста уже присутствовали в библиографии.
- Выполнена сборка из `text_coursework/final_report_work/` командой `latexmk main.tex`; сборка завершилась с кодом `0`, PDF обновлен.
- После сборки выполнено `latexmk -c main.tex`: служебные LaTeX-файлы удалены, `main.pdf` оставлен.
- Нефатальные предупреждения сборки: `Underfull \hbox` на титульном листе и в библиографии, `Overfull \hbox` во вставленном введении на длинной строке с перечислением моделей. Текст не переносился вручную, чтобы не менять предоставленное содержимое.

## Section layout and protocol update 2026-05-30

- Изменены файлы: `main.tex`, `sections/01_introduction.tex`, `sections/04_experiment_protocol.tex`, `notes/logs/SKELETON_BUILD_LOG.md`, `main.pdf`.
- Во введение добавлена короткая фраза про преобразование атомистических данных между форматами, используемыми MTP, MACE и MatterSim.
- В раздел 4 добавлена подглава `Преобразование форматов данных`.
- В `main.tex` добавлены `\clearpage` перед главами 1--7; основные главы теперь начинаются с новой страницы, подглавы не отделялись новой страницей.
- Выполнена сборка из `text_coursework/final_report_work/` командой `latexmk -g main.tex`; сборка завершилась с кодом `0`, `main.pdf` обновлен.
- Новое предупреждение LaTeX после добавления подглавы: `Overfull \hbox (29.42638pt too wide)` в `sections/04_experiment_protocol.tex` на строках 13--14. Существующие предупреждения `Underfull \hbox` на титульном листе и в библиографии сохранились.

## Problem statement and metrics update 2026-05-30

- Изменены файлы: `main.tex`, `sections/02_problem_metrics.tex`, `notes/logs/SKELETON_BUILD_LOG.md`, `main.pdf`.
- В `sections/02_problem_metrics.tex` placeholder-текст заменен на предоставленный пользователем текст раздела `Постановка задачи и метрики`.
- Содержательные формулировки пользователя не изменялись.
- Для компиляции LaTeX выполнены только синтаксические правки математической разметки: inline-фрагменты вида `(...)` переведены в `$...$`, display-фрагменты вида `[...]` переведены в `\[...\]`, маркеры `*` в индексах формул заменены на `_`, имена разбиений `test_300K`, `test_600K`, `test_1200K` оформлены как `\texttt{...}` с экранированными подчеркиваниями, запись температуры оформлена как `$300\,\mathrm{K}$`.
- В `main.tex` добавлен пакет `amsfonts`, необходимый для `\mathbb{R}` во вставленном разделе.
- Выполнена сборка из `text_coursework/final_report_work/` командой `latexmk -g main.tex`; сборка завершилась с кодом `0`, `main.pdf` обновлен.
- Новых предупреждений, связанных с разделом 2, в финальном проходе не появилось. Сохранились ранее известные предупреждения: `Underfull \hbox` на титульном листе, `Overfull \hbox (29.42638pt too wide)` в `sections/04_experiment_protocol.tex`, `Underfull \hbox` в библиографии.
- По последующей правке пользователя из раздела 2 удалено моноширинное оформление `\texttt{...}` для `test_300K`, `test_600K`, `test_1200K`; названия разбиений оставлены обычным текстом с экранированными подчеркиваниями.
- Формулы раздела 2 проверены: силы заданы как минус градиент энергии, метрики энергии усредняются по конфигурациям для ошибки на атом, метрики сил усредняются по всем атомам и трем координатным компонентам.
- Повторная сборка `latexmk -g main.tex` завершилась с кодом `0`, `main.pdf` обновлен.

## Problem metrics wording cleanup 2026-05-30

- Изменены файлы: `sections/02_problem_metrics.tex`, `notes/logs/SKELETON_BUILD_LOG.md`, `main.pdf`.
- В разделе 2 названия разбиений `test_300K`, `test_600K`, `test_1200K` оставлены обычным текстом без моноширинного выделения.
- Формулировка `Train-метрики` заменена на `Метрики на обучающем разбиении`, чтобы не смешивать английское имя split с русским текстом.
- Обозначения метрик сил в формулах заменены с `MAE_F`/`RMSE_F` на `MAE_{forces}`/`RMSE_{forces}`; в тексте англоязычные `Energy MAE`, `Forces RMSE` и аналогичные заменены на `MAE по энергии`, `RMSE по энергии`, `MAE по силам`, `RMSE по силам`.
- Смысл формул не менялся. Проверка по источникам: статья M3GNet задает силы как `f = -dE/dx`; код MACE считает `MAE` как среднее `abs(delta)` и `RMSE` как `sqrt(mean(square(delta)))`; MatterSim model card описывает отдельные MAE для энергии, сил и stress с энергией в eV/atom и силами в eV/A.
- Выполнена сборка из `text_coursework/final_report_work/` командой `latexmk -g main.tex`; сборка завершилась с кодом `0`, `main.pdf` обновлен.
- Новых предупреждений LaTeX, связанных с разделом 2, не появилось. Сохранились ранее известные предупреждения: `Underfull \hbox` на титульном листе, `Overfull \hbox (29.42638pt too wide)` в `sections/04_experiment_protocol.tex`, `Underfull \hbox` в библиографии.

## Force notation style fix 2026-05-30

- Изменены файлы: `sections/02_problem_metrics.tex`, `notes/logs/SKELETON_BUILD_LOG.md`, `main.pdf`.
- В разделе 2 жирное векторное обозначение `\mathbf{F}` заменено на обычное `F` для эталонных сил, предсказанных сил и формулы силы через градиент.
- Содержательный смысл формулы не менялся: силы по-прежнему записаны как минус градиент энергии по координатам.
- Выполнена сборка из `text_coursework/final_report_work/` командой `latexmk -g main.tex`; сборка завершилась с кодом `0`, `main.pdf` обновлен.
- Новых предупреждений LaTeX, связанных с этой правкой, не появилось. Сохранились ранее известные предупреждения: `Underfull \hbox` на титульном листе, `Overfull \hbox (29.42638pt too wide)` в `sections/04_experiment_protocol.tex`, `Underfull \hbox` в библиографии.

## Literature and models section replacement 2026-05-30

- Изменены файлы: `sections/03_methods_literature.tex`, `ref.bib`, `notes/logs/SKELETON_BUILD_LOG.md`, `main.pdf`.
- Раздел 3 заменен на расширенную версию `Обзор литературы и используемые модели` с формулами для локального разложения энергии, MTP, M3GNet, MatterSim, MACE и общей записи сравниваемых стратегий.
- Источник `podryabinkin2023mlip3` сохранен в `ref.bib` и используется в `sections/03_methods_literature.tex` как контекст по линии MLIP-пакетов и активному обучению MTP, а не как описание конкретной версии MLIP-4.
- В MTP-подразделе сохранено разграничение: `shapeev2016mtp` используется для математической основы MTP, `mlip4software` для использованного MLIP-4, `podryabinkin2023mlip3` для контекста MLIP-3.
- Для `RadialBasisCinf(size=8)` добавлен только версточный разрыв через `\allowbreak`, чтобы убрать сильный `Overfull \hbox`; смысл текста не менялся.
- Выполнена сборка командой `python3 scripts/compile_latex.py ... --compiler texlive --engine xelatex`; сборка завершилась с кодом `0`, `main.pdf` обновлен.
- BibTeX использовал 8 записей из `ref.bib`; warning-ов BibTeX и undefined citation warnings нет.
- Нефатальные предупреждения после финальной сборки: `Underfull \hbox` на титульном листе и в библиографии; небольшие `Overfull \hbox (0.80939pt too wide)` и `Overfull \hbox (0.85616pt too wide)` в `sections/03_methods_literature.tex`; ранее известный `Overfull \hbox (29.42638pt too wide)` в `sections/04_experiment_protocol.tex`.
