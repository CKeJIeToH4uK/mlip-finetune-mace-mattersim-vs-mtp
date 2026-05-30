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

## Typography cleanup 2026-05-30

- Убрано моноширинное выделение `RadialBasisCinf(size=8)` в `sections/03_methods_literature.tex`; выражение теперь набирается обычным текстом.
- В активных файлах статьи `main.tex` и `sections/*.tex` заменены LaTeX-тройки дефисов на типографское тире в исходнике.
- Проверка `rg` подтвердила: в активных файлах статьи больше нет LaTeX-троек дефисов, а в файлах `sections/*.tex` нет `\texttt{...}` и `\textbf{...}`.
- Выполнена сборка командой `python3 scripts/compile_latex.py ... --compiler texlive --engine xelatex`; сборка завершилась с кодом `0`, `main.pdf` обновлен.

## Section 3 compression 2026-05-30

- Сокращен `sections/03_methods_literature.tex`: раздел 3 переписан как компактный архитектурный обзор вместо подробного вывода промежуточных формул M3GNet, MatterSim и MACE.
- В `3.1` оставлена одна формула локального разложения энергии; отдельные display-формулы для энергии и сил удалены, потому что связь сил с градиентом уже задана в разделе 2.
- В MTP оставлены формулы моментного тензора и атомной энергии через базис, а также абзац про MTP-16/MTP-20, 122/390 базисных функций и числа параметров по organic, H2O и MoNbTaVW. Абзац про MLIP-4/MLIP-3 сокращен до двух предложений.
- В M3GNet оставлены формулы `G=(V,E,X,[M,u])`, короткое трехчастичное обновление через атом `k` и силы `f=-dE/dx`; удалены spherical Bessel/spherical harmonics, edge update, atom update, stress и loss formula.
- В MatterSim удалены `X -> kappa_G -> E` и две MLP-формулы; оставлен текст про широкое предобучение, M3GNet/Graphormer и осторожность по контрольным точкам модели.
- В MACE оставлены общее сообщение, условие эквивариантности и формула сообщений повышенного порядка; удалены node state, update/readout, A/B features, final message, MACE update и energy readout.
- Добавлена подглава `Тонкая настройка универсальных моделей` с одной формулой objective и явным разграничением MACE default и MACE-EW50 как разных протоколов.
- Выполнена сборка командой `latexmk -g main.tex`; сборка завершилась с кодом `0`, `main.pdf` обновлен. Готовый PDF содержит 16 страниц; раздел 3 занимает 4 страницы до начала раздела 4.
- Проверены ссылки и labels: 8 used / 8 defined citation keys, missing/unused нет, duplicate labels нет.
- Нефатальные предупреждения после сборки: `Underfull \hbox` на титульном листе и в библиографии; ранее известный `Overfull \hbox (29.42638pt too wide)` в `sections/04_experiment_protocol.tex`.
- Проведены две независимые read-only агентские проверки по 3 прохода каждая. Проверки подтвердили структуру раздела, целевой объем, корректность citations/labels, отсутствие `---`, `\texttt`, `\textbf` и literal `checkpoint` в разделе 3. Единственное замечание: фраза `контрольным точкам модели` является русской заменой `checkpoint`; оставлена как терминологически согласованная с задачей.

## Section 3 style cleanup 2026-05-30

- В MatterSim-подразделе заменено слово `backbone` на русскую формулировку `архитектурную основу`.
- В `sections/03_methods_literature.tex` убраны жирные математические обозначения `\mathbf{...}`; заголовки не менялись.
- Выполнена сборка командой `python3 scripts/compile_latex.py ... --compiler texlive --engine xelatex`; сборка завершилась с кодом `0`, `main.pdf` обновлен.
- Проверка `rg` подтвердила отсутствие `backbone`, `\mathbf`, `\boldsymbol`, `\bm`, `\textbf` и `\texttt` в разделе 3. Citations/labels без изменений: missing/unused citation keys нет, duplicate labels нет.

## Experiment protocol section update 2026-05-30

- `sections/04_experiment_protocol.tex` заменен на содержательный раздел `Экспериментальный протокол`: добавлены общий цикл эксперимента, данные и разбиения, сравниваемые режимы обучения, таблицы по системам/режимам и блок про преобразование форматов данных.
- Таблицы оформлены через `tabularx` с переносимыми колонками, чтобы не возвращать прежний `Overfull \hbox` в разделе 4.
- В тексте сохранены разграничения: organic-датасет интерпретируется как перенос между температурными режимами; H2O и MoNbTaVW — как отложенная валидация; MACE default и MACE-EW50 описаны как разные протоколы.
- Англо-русские склейки вроде `validation-разбиении` заменены на русские формулировки, кроме технических имен разбиений `train`, `valid`, `test_300K`, `test_600K`, `test_1200K` в таблицах и описании split-ов.
- Выполнена сборка командой `python3 scripts/compile_latex.py ... --compiler texlive --engine xelatex`; сборка завершилась с кодом `0`, `main.pdf` обновлен.
- Проверены citations/labels: missing/unused citation keys нет, duplicate labels нет. `git diff --check` без замечаний.
- После правки `Overfull` warnings не осталось; сохраняются только `Underfull \hbox` на титульном листе и в таблице 2.

## Experiment protocol and appendix rebuild 2026-05-30

- `sections/04_experiment_protocol.tex` пересобран в компактную структуру из четырех подглав: данные и контрольные разбиения, подготовка данных и преобразование форматов, режимы обучения и оценки, расчет метрик и границы воспроизводимости.
- В разделе 4 сохранены ключевые разграничения: organic-датасет оценивается по температурному переносу, H2O и MoNbTaVW — по валидационному разбиению, MACE default и MACE-EW50 остаются разными протоколами, оценки без дообучения описаны только как диагностический режим.
- Англоязычные служебные формулировки в прозе заменены на русские: `provenance`, `source chain`, `checkpoint`, `fine-tuning`, `baseline`, `zero-shot` не встречаются в активном тексте раздела 4 и приложений, кроме технических имен файлов и LaTeX labels.
- `sections/appendix.tex` заменен с заглушки на приложения A–E: полные таблицы метрик, дополнительные протоколы и абляционные проверки, преобразование форматов, цепочка происхождения результатов, границы воспроизводимости.
- Длинные пути и таблицы приложений сжаты до проверяемых меток и имен файлов, чтобы убрать переполнения строк.
- Выполнена сборка командой `python3 scripts/compile_latex.py ... --compiler texlive --engine xelatex`; сборка завершилась с кодом `0`, `main.pdf` обновлен.
- После дополнительного сжатия раздел 4 занимает страницы 12--14 PDF, то есть укладывается в целевые 3 страницы.
- После финальной сборки `Overfull \hbox` warnings нет. Сохраняются только `Underfull \hbox` на титульном листе и в библиографии, а также стандартные предупреждения LaTeX о переносе нескольких таблиц с `[h]` на `[ht]`.
- По последующей типографской правке снято моноширинное выделение с `.cfg` в разделе 4 и приложении; повторная сборка `python3 scripts/compile_latex.py ... --compiler texlive --engine xelatex` завершилась с кодом `0`, `main.pdf` обновлен.
- По последующей типографской правке снято моноширинное оформление `\path{...}` со списка CSV/MD-файлов и имен скриптов в приложении; видимые имена файлов оставлены обычным текстом с экранированными подчеркиваниями. Повторная сборка завершилась с кодом `0`, `Overfull \hbox` warnings нет.
- В `main.tex` добавлен явный `\clearpage` перед `\appendix`, чтобы приложения начинались с отдельной страницы после списка источников. Сборка завершилась с кодом `0`; по проверке текстового слоя PDF список источников заканчивается на странице 17, приложение A начинается на странице 18.

## Experiment protocol final review tweaks 2026-05-30

- В разделе 4 порядок систем приведен к основной последовательности отчета: organic-датасет, H2O, MoNbTaVW; предложение укорочено, чтобы не вернуть `Overfull \hbox`.
- Формулировка про форматы данных уточнена: `ASE/extxyz` и `.cfg` оформлены как технические форматы, `.cfg` описан как формат, используемый в MLIP.
- Вместо обобщенного `test-разбиениям` перечислены конкретные контрольные разбиения organic-датасета: `test_300K`, `test_600K`, `test_1200K`.
- Выполнена сборка командой `python3 scripts/compile_latex.py ... --compiler texlive --engine xelatex`; сборка завершилась с кодом `0`, `main.pdf` обновлен.
- После сборки `Overfull \hbox`, undefined citations и duplicate labels нет. Сохраняются только ранее известные `Underfull \hbox` на титульном листе и в библиографии, а также предупреждения LaTeX о переносе таблиц с `[h]` на `[ht]`.
