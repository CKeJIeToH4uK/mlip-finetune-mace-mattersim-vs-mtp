# GPT Slide Handoff

Use this when asking GPT in the browser to create the next architecture slide.
For parallel work, use worker mode first: every worker owns one slide number and must not edit shared registries. After workers finish, use integrator mode once.

```text
WORKER MODE

Ты создаёшь один новый LaTeX/Beamer слайд для архитектурного блока презентации.
Тебе заранее назначены:
- номер слайда XX;
- short_name;
- итоговый файл sections/arch_XX_short_name.tex.

Проект устроен так:
- исходники слайдов лежат в 05_deck/sections/
- архитектурный блок собирается через 05_deck/sections/03_methods_architecture.tex
- общий preview собирается из 05_deck/main_architecture_preview.tex
- PDF и PNG должны лежать в 06_build/
- служебные LaTeX-файлы должны уходить в 06_build/latex_aux/previews/arch_XX/

Правила для нового слайда:
1. Создай отдельный файл:
   05_deck/sections/arch_XX_short_name.tex
2. Создай отдельный preview file:
   05_deck/main_arch_XX_preview.tex
3. Внутри section-файла должен быть ровно один \begin{frame}...\end{frame}.
4. Не добавляй \section, title slide или Plan slide.
5. Не меняй template, header.tex и уже готовые слайды.
6. Не меняй shared files:
   - 05_deck/sections/03_methods_architecture.tex
   - 05_deck/main_architecture_preview.tex
   - 03_content/deck_status.md
   - чужие arch_YY_*.tex
7. Используй тот же стиль:
   - HSE Beamer template;
   - белый фон;
   - синий / бирюзовый / серый;
   - аккуратный TikZ;
   - минимум текста;
   - без случайных картинок и чёрного фона.
8. Собери только индивидуальный preview:
   cd 05_deck
   mkdir -p ../06_build/latex_aux/previews/arch_XX
   xelatex -interaction=nonstopmode -halt-on-error -output-directory=../06_build/latex_aux/previews/arch_XX main_arch_XX_preview.tex
   xelatex -interaction=nonstopmode -halt-on-error -output-directory=../06_build/latex_aux/previews/arch_XX main_arch_XX_preview.tex
   cp ../06_build/latex_aux/previews/arch_XX/main_arch_XX_preview.pdf ../06_build/main_arch_XX_preview.pdf
9. Если есть pdftoppm:
   mkdir -p ../06_build/arch_XX_preview
   pdftoppm -png -singlefile ../06_build/main_arch_XX_preview.pdf ../06_build/arch_XX_preview/arch_XX

Перед ответом проверь:
- индивидуальный PDF собирается;
- PDF содержит ровно 1 страницу;
- нет auto Plan slide;
- нет слов “generated”, “GPT”, “DALL-E”, “AI”, “Figure adapted from project context”;
- нет “эволюционной геномики”;
- footer: “Научно-учебная группа «Машинное обучение в атомистическом моделировании»”;
- схема не вылезает за края;
- текст читаемый.

В ответе перечисли только свои файлы и preview paths.
```

```text
INTEGRATOR MODE

Ты интегрируешь уже готовые architecture slides.
Не меняй содержимое отдельных arch_XX_*.tex, если нет отдельной просьбы.

1. Проверь готовые файлы section и индивидуальные preview.
2. Добавь новые слайды в:
   05_deck/sections/03_methods_architecture.tex
   строками вида:
   \input{sections/arch_XX_short_name}
3. Собери общий preview:
   cd 05_deck
   xelatex -interaction=nonstopmode -halt-on-error main_architecture_preview.tex
   xelatex -interaction=nonstopmode -halt-on-error main_architecture_preview.tex
   cp main_architecture_preview.pdf ../06_build/main_architecture_preview.pdf
4. Если есть pdftoppm:
   mkdir -p ../06_build/architecture_preview
   pdftoppm -png ../06_build/main_architecture_preview.pdf ../06_build/architecture_preview/architecture
5. Проверь:
   - общий PDF собирается;
   - количество страниц соответствует registry;
   - нет auto Plan slide;
   - footer правильный;
   - новые слайды в нужном порядке.
```
