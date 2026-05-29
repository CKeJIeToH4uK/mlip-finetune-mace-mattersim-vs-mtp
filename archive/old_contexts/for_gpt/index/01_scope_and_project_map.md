# Scope and Project Map

## Root summary

В корне проекта лежат материалы курсовой и сопутствующих экспериментов: датированные папки с результатами (`19.03.26`, `26.02.26`, `02.04.26`, `Кт1`), две папки презентаций (`pres_research1`, `pres_mace`), PDF-файлы с заданием и референсами (`task_mannanov.pdf`, `mattersim.pdf`, `mace.ipynb.pdf`, `m3gnet.pdf`), основной рабочий репозиторий `repo/` и служебная зона для индексирования `for_gpt/`.

Наиболее вероятный центр фактов для итогового доклада - `repo/coursework` вместе с уже агрегированными срезами `19.03.26` и `26.02.26`. Тяжелые исходные данные, чекпоинты, локальные сборки, MLIP/LAMMPS source trees, шрифты и `.git` нужно исключить из дальнейшего анализа.

PDF-файлы на P1 проверялись только по имени, размеру и типу файла, без извлечения полного содержимого.

## Likely relevant folders

| path | why relevant | expected content | priority |
|---|---|---|---|
| `task_mannanov.pdf` | Вероятно, формальная постановка задачи курсовой. | 1-страничный PDF с требованиями и рамками работы. | A |
| `repo/coursework` | Главная рабочая зона курсовой. | Скрипты, sbatch-файлы, базовые eval, MACE/MatterSim/MTP результаты, датасеты и артефакты. | A |
| `repo/coursework/cross_temp_eval` | Компактная зона кросс-температурной оценки. | JSON-результаты для MACE, MatterSim, MTP на 300K/600K/1200K, eval-скрипты и slurm logs. | A |
| `repo/coursework/initial_eval` | Базовые zero-shot/initial результаты. | Результаты `mace_base`, `mattersim_base`, `mtp_init`, small JSON/TXT. | A |
| `repo/coursework/new_datasets` | Расширение на alloy/water, вероятно важное для финального сравнения. | `alloy`, `water`, `data`, `figures`, `analysis_v2.ipynb`; внутри есть результаты и тяжелые модели. | A |
| `repo/coursework/new_datasets/figures` | Готовые графики для доклада. | PNG с MAE/RMSE, loss curves, cross-temp organic. | A |
| `19.03.26` | Датированный срез уже собранных графиков и текущего cross-temp eval. | `analysis.ipynb`, PNG-графики, `cross_temp_eval_300_600_1200K_current`, epoch-vs-error папки. | A |
| `26.02.26` | Датированный срез экспериментов и агрегированных CSV. | `sweep_lr_bs_summary.csv`, `mtp_errors_summary.csv`, `epoch_vs_err_curve.csv`, logs, finetune folders. | A |
| `pres_research1` | Презентация с заголовком `Finetuning M3GNet`; вероятно отражает раннюю структуру доклада. | `main.tex`, `main.pdf`, `pictures`, LaTeX build logs, fonts/theme. | A |
| `pres_mace` | Презентация с заголовком `Архитектура MACE и Fine-tuning`. | `main.tex`, `speech.tex`, `РАЗБОР_СЛАЙДОВ.md`, `main.pdf`, LaTeX build logs. | A |
| `repo/coursework/mtp_runs` | Компактные MTP train/eval результаты. | `metrics.json`, trained MTP JSON, slurm outputs, training scripts. | B |
| `repo/coursework/mattersim_eval` | Ранний MatterSim eval. | Small JSON/TXT result and warning log. | B |
| `02.04.26` | Небольшой датированный срез анализа. | `analysis_v2.ipynb`; не запускать, можно индексировать метаданные/структуру. | B |
| `Кт1` | Ранний/учебный этап с MatterSim и MTP логами. | Eval JSON/TXT, logs, scripts, sbatch, notebooks. | B |
| `repo/coursework/FLiNaK` | Дополнительный MatterSim fine-tuning task по FLiNaK; может быть полезен как поздний пример пайплайна. | `README.md`, `eval/summary.md`, data, scripts, run dirs. | B |
| `repo/coursework/FLiNaK/eval` | Компактная итоговая зона FLiNaK. | `summary.md`, `zero_shot_all.json`, `ft_all_on_all.json`, `ft_split_on_valid.json`. | B |
| `mattersim.pdf` | Референс по MatterSim. | PDF, около 37M. | B |
| `m3gnet.pdf` | Референс по M3GNet. | PDF, около 12M. | B |
| `mace.ipynb.pdf` | PDF-экспорт ноутбука или материала по MACE. | PDF, 14 страниц, около 404K. | B |
| `repo/coursework/databases` | Источник данных для текущих 300K тестов, но не место для полного чтения. | `.cfg`, `.xyz`, `.json` датасеты и температурные подпапки. | C |
| `repo/data` | Дубликат/центральное хранилище датасетов. | `.cfg`, `.xyz`, `.json` для 300K/600K/1200K, H2O, MoNbTaVW. | C |
| `for_gpt` | Рабочая зона дальнейшего анализа. | Индексы, таблицы, markdown-отчеты, небольшие вспомогательные скрипты. | C |

## Likely irrelevant / ignore folders

| path | reason to ignore | risk if included |
|---|---|---|
| `repo/.git` | Git internals, не научное содержание. | Много шума, object hashes, риск огромного нерелевантного индекса. |
| `.DS_Store` / `**/.DS_Store` | macOS metadata. | Шум в индексах. |
| `.claude`, `.vscode` | Локальные настройки инструментов. | Не относятся к курсовой, могут увести в конфиги. |
| `repo/work` | Рабочие source/build деревья MLIP/LAMMPS. | 2.5G нерелевантного кода и сборочных файлов. |
| `repo/work/mlip_clean/lammps` | LAMMPS source tree. | Огромный объем внешнего кода, не источник результатов доклада. |
| `repo/work/mlip_clean/lammps_uncompiled` | Еще одно LAMMPS source tree. | Дублирование и шум. |
| `repo/work/mlip_clean/mlip-4` | MLIP source tree. | Внешний код, не курсовые результаты. |
| `repo/work/mlip_clean/interface-lammps-mlip-4` | Интерфейсный source tree. | Сборочная инфраструктура вместо результатов. |
| `repo/local` | Локальные бинарники/установки. | Можно случайно индексировать бинарные артефакты. |
| `pres_research1/font`, `pres_mace/font` | Шрифты презентаций. | Копирование/индексация шрифтов запрещены и не нужны. |
| `pres_research1/beamerthemesrc`, `pres_mace/beamerthemesrc` | Тема Beamer, не предметное содержание. | Шум LaTeX-оформления. |
| `repo/coursework/checkpoints`, `26.02.26/checkpoints` | Чекпоинты MACE/MatterSim. | `.pt`/`.model` запрещено трогать; высокий риск тяжелых файлов. |
| `repo/coursework/mace_models`, `26.02.26/mace_models` | Предобученные/сохраненные модели MACE. | `.model` файлы, не читать и не копировать. |
| `repo/coursework/new_datasets/*/mace/checkpoints` | Чекпоинты MACE для alloy/water. | `.pt`/`.model` файлы. |
| `repo/coursework/new_datasets/*/mattersim/finetune_result` | Чекпоинты MatterSim. | `.pth` файлы, очень тяжелые. |
| `repo/coursework/FLiNaK/run_all`, `repo/coursework/FLiNaK/run_split` | Run dirs с логами и чекпоинтами. | 395M вместе; часть содержит модели/чекпоинты. |
| `**/__pycache__` | Python bytecode cache. | Нерелевантный бинарный мусор. |
| `**/build`, `**/build-*`, `**/cmake-build-*` | Сборочные директории. | Много внешних артефактов. |
| `*.xyz`, `*.cfg`, large `*.json` datasets | Сырые датасеты, разрешены только имена/размеры. | Токеновый взрыв и нарушение запрета на открытие больших датасетов. |

## Coursework-related areas

### Dated folders

`19.03.26` - срез на 698M. Содержит готовые PNG-графики (`cross_temp_*`, `initial_force_errors.png`, `rmse_f_vs_temperature.png`, `training_curves_comparison.png`), `analysis.ipynb`, компактный `cross_temp_eval_300_600_1200K_current` и две тяжелые epoch-vs-error папки. Для следующих P-задач стоит индексировать готовые графики, `results/*.json`, small logs/resources; не запускать ноутбук и не читать модели.

`26.02.26` - срез на 2.4G. Важны агрегированные CSV: `sweep_lr_bs_summary.csv`, `sweep_lr_bs_history.csv`, `mtp_errors_summary.csv`, `epoch_vs_err_curve.csv`, `ensemble_logs16_stats.csv`, `ensemble_logs20_stats.csv`. Основной риск - `mattersim_finetune` на 2.3G и checkpoint/model folders. Дальше читать только summary CSV, small logs и small JSON/TXT результатов.

`02.04.26` - маленькая папка на 2.1M с `analysis_v2.ipynb`. Вероятно связана с `repo/coursework/new_datasets/analysis_v2.ipynb`. Не запускать; можно позже извлечь структуру/метаданные notebook или сопоставить с готовыми фигурами.

`Кт1` - ранний/учебный блок на 6.8M. Содержит MatterSim script/sbatch, eval JSON/TXT, MTP logs, warning logs и notebooks. Полезно для хронологии и ранних baseline, но не должно вытеснять более поздние `repo/coursework` и `19.03.26`.

### Presentations

`pres_research1` - презентация на 6.6M, title в `main.tex`: `Finetuning M3GNet`. Основные файлы для анализа: `main.tex`, `main.pdf`, возможно `pictures/`. Игнорировать `font/`, `beamerthemesrc/` и LaTeX build artifacts, кроме случаев диагностики ссылок на картинки.

`pres_mace` - презентация на 1.2M, title в `main.tex`: `Архитектура MACE и Fine-tuning`. Основные файлы: `main.tex`, `speech.tex`, `РАЗБОР_СЛАЙДОВ.md`, `main.pdf`. Это вероятный source-of-truth для объяснения MACE и структуры выступления.

### repo/coursework

`repo/coursework` - основная зона на 4.5G. На верхнем уровне есть small scripts (`base_mattersim.py`, `cfg_to_json.py`, `xyz_to_mtp_json.py`, `mtp.py`, sbatch scripts), eval folders (`initial_eval`, `cross_temp_eval`, `mattersim_eval`, `mtp_runs`), run/log folders (`logs*`, `mace_finetune`, `mattersim_finetune`) и data/model folders (`databases`, `checkpoints`, `mace_models`, `new_datasets`). Следующий анализ должен начинаться с компактных result folders и summary files, а не с raw data/model dirs.

### repo/coursework/new_datasets

`repo/coursework/new_datasets` - зона на 1.3G с двумя новыми задачами: `alloy` и `water`. Есть готовые `figures/` на 1.2M и raw/converted data в `data/`, `alloy/convert`, `water/convert`. Внутри `alloy/mace`, `alloy/mattersim`, `alloy/mtp`, `water/mace`, `water/mattersim`, `water/mtp` лежат eval JSON, train logs, sbatch/scripts и тяжелые модели. Для доклада брать `figures/*.png`, `eval_train.json`, `eval_valid.json`, `metrics*.json`, logs summaries; обходить `finetune_result`, `checkpoints`, `.pth`, `.pt`, `.model`.

### repo/coursework/cross_temp_eval

`repo/coursework/cross_temp_eval` - компактная зона на 1.1M. Структура: `results/{mace,mattersim,mtp}`, `scripts`, `sbatch`, `slurm_logs`. В `results` лежат small JSON для 300K/600K/1200K; это сильный кандидат на финальную таблицу кросс-температурного сравнения.

## Heavy folders to avoid

| path | approximate size if available | why avoid |
|---|---:|---|
| `repo/coursework` | 4.5G | Важная верхняя зона, но глубокий обход упрется в datasets/checkpoints/log trees. |
| `repo/work` | 2.5G | Source/build tree, не курсовые результаты. |
| `repo/work/mlip_clean` | 2.5G | LAMMPS/MLIP source trees. |
| `26.02.26/mattersim_finetune` | 2.3G | Raw MatterSim fine-tuning runs; читать только summary/small logs. |
| `repo/coursework/mattersim_finetune` | 2.3G | Raw MatterSim fine-tuning runs; возможны тяжелые модели/логи. |
| `repo/coursework/new_datasets` | 1.3G | Важна, но внутри есть raw data и checkpoints. |
| `repo/coursework/new_datasets/alloy` | 924M | Основной вес в MatterSim checkpoints. |
| `repo/coursework/new_datasets/alloy/mattersim` | 870M | `finetune_result` с `.pth` checkpoint files. |
| `19.03.26` | 698M | Важный срез, но две epoch-vs-error папки тяжелые. |
| `19.03.26/epoch_vs_err_mattersim` | 377M | Raw training run; брать только selected logs/results. |
| `19.03.26/epoch_vs_err_25_mace` | 318M | Raw training run; брать только selected logs/results. |
| `repo/coursework/FLiNaK` | 404M | Важен README/eval, но run dirs heavy. |
| `repo/coursework/FLiNaK/run_all` | 206M | MatterSim run artifacts/checkpoints. |
| `repo/coursework/FLiNaK/run_split` | 189M | MatterSim run artifacts/checkpoints. |
| `repo/coursework/new_datasets/water` | 271M | Есть eval и logs, но также model artifacts. |
| `repo/local` | 101M | Локальные бинарники/установки. |
| `repo/data` | 97M | Raw datasets; не открывать содержимое. |
| `repo/.git` | 84M | Git internals. |
| `repo/coursework/databases` | 64M | Raw datasets and converted JSON. |
| `repo/coursework/checkpoints` | 45M | `.pt`/`.model` artifacts. |
| `26.02.26/checkpoints` | 45M | `.pt`/`.model` artifacts. |
| `repo/coursework/mace_models` | 31M | `.model` artifacts. |
| `26.02.26/mace_models` | 31M | `.model` artifacts. |
| `mattersim.pdf` | 37M | Reference PDF; extract only if needed later, not in bulk. |
| `m3gnet.pdf` | 12M | Reference PDF; extract only targeted pages/metadata if needed later. |

## Candidate source-of-truth areas

| path | why it may be source of truth | what to inspect next |
|---|---|---|
| `task_mannanov.pdf` | Formal task statement and grading target. | Extract/summarize assignment constraints in a small markdown note. |
| `pres_research1/main.tex` | Existing narrative for `Finetuning M3GNet`. | Index slide titles, claims, referenced figures. |
| `pres_mace/main.tex`, `pres_mace/speech.tex`, `pres_mace/РАЗБОР_СЛАЙДОВ.md` | Existing narrative for MACE architecture/fine-tuning. | Extract slide outline and speaking points. |
| `repo/coursework/cross_temp_eval/results` | Compact final metrics for cross-temperature comparison. | Normalize JSON metrics into a CSV table. |
| `repo/coursework/initial_eval/results` | Baseline metrics before fine-tuning. | Normalize baseline metrics and link to cross-temp table. |
| `19.03.26/cross_temp_eval_300_600_1200K_current/results` | Dated copy of current cross-temp eval. | Compare with `repo/coursework/cross_temp_eval/results` for duplicates/divergence. |
| `19.03.26/*.png` | Ready-made figures for report/presentation. | Build figure inventory with captions and metric provenance. |
| `26.02.26/sweep_lr_bs_summary.csv` | Aggregated hyperparameter sweep metrics. | Identify best lr/batch by validation loss/MAE. |
| `26.02.26/mtp_errors_summary.csv` | Aggregated MTP errors from logs. | Produce concise MTP train/valid summary. |
| `26.02.26/epoch_vs_err_curve.csv` | Epoch-vs-error curve already collected. | Map to training curves and final plot. |
| `repo/coursework/new_datasets/figures` | Ready-made figures for alloy/water results. | Inventory plots and connect to source eval JSON. |
| `repo/coursework/new_datasets/{alloy,water}/{mace,mattersim,mtp}` | Per-model results for new datasets. | Index only eval JSON, metrics JSON, logs; avoid model/checkpoint files. |
| `repo/coursework/mtp_runs/*/metrics.json` | Compact MTP training metrics. | Merge level16/level20 metrics into comparison table. |
| `repo/coursework/FLiNaK/README.md` | Documents a later MatterSim fine-tuning pipeline and intent. | Decide whether FLiNaK belongs to final coursework scope. |
| `repo/coursework/FLiNaK/eval/summary.md` | Compact FLiNaK result summary. | If in scope, normalize metrics and note dataset details. |

## Immediate next indexing tasks

1. Create `02_assignment_and_requirements.md`: targeted extraction/summarization of `task_mannanov.pdf`.
2. Create a presentation index for `pres_research1/main.tex`, `pres_mace/main.tex`, `pres_mace/speech.tex`, and `pres_mace/РАЗБОР_СЛАЙДОВ.md`.
3. Normalize `repo/coursework/cross_temp_eval/results/**/*.json` into a single CSV of metrics by model and temperature.
4. Normalize `repo/coursework/initial_eval/results/**/*.{json,txt}` into a baseline metrics table.
5. Compare `repo/coursework/cross_temp_eval/results` with `19.03.26/cross_temp_eval_300_600_1200K_current/results` to detect duplicates or newer copies.
6. Index all ready-made figures in `19.03.26/*.png` and `repo/coursework/new_datasets/figures/*.png` with candidate captions.
7. Summarize `26.02.26/sweep_lr_bs_summary.csv`, `sweep_lr_bs_history.csv`, `epoch_vs_err_curve.csv`, and `mtp_errors_summary.csv`.
8. Index `repo/coursework/new_datasets/{alloy,water}` using only eval JSON, metrics JSON, logs, sbatch/scripts, and figures; skip raw datasets and checkpoints.
9. Build a dataset metadata map from file names/sizes only for `repo/data`, `repo/coursework/databases`, and `repo/coursework/new_datasets/data`.
10. Decide whether `repo/coursework/FLiNaK` is in final-report scope; if yes, index only `README.md` and `eval/summary.md`.
11. Create a reusable ignore-pattern file for future P-tasks: `.git`, `repo/work`, `repo/local`, fonts, checkpoints, model files, raw datasets, build dirs, `__pycache__`.
12. Create a reference-literature map for `mattersim.pdf`, `m3gnet.pdf`, and `mace.ipynb.pdf` using only targeted metadata/page extraction when needed.
