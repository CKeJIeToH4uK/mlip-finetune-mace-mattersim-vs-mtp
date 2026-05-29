# Parallel Slide Workflow

Goal:
- allow several agents to work on different architecture slides at the same time;
- avoid write conflicts and build-output races;
- keep one deterministic integration point for the final architecture block.

## Ownership Model

Each slide worker owns exactly one slide namespace:

- `05_deck/sections/arch_XX_short_name.tex`
- `05_deck/main_arch_XX_preview.tex`
- `06_build/main_arch_XX_preview.pdf`
- `06_build/arch_XX_preview/arch_XX.png`
- optional assets only under `04_assets/.../arch_XX/`
- optional aux files only under `06_build/latex_aux/previews/arch_XX/`

The integrator owns shared files:

- `05_deck/sections/03_methods_architecture.tex`
- `05_deck/main_architecture_preview.tex`
- `06_build/main_architecture_preview.pdf`
- `06_build/architecture_preview/`
- `03_content/deck_status.md`

Workers must not edit shared files. In particular, workers must not edit:

- `05_deck/sections/03_methods_architecture.tex`
- any existing `arch_YY_*.tex` where `YY != XX`
- `main_architecture_preview.tex`
- template/header files
- shared build previews in `06_build/architecture_preview/`

## Safe Parallel Protocol

1. The integrator assigns slide numbers and filenames before work starts.
   Example:
   - Worker A: `arch_04_message_passing.tex`
   - Worker B: `arch_05_readout_energy_forces.tex`

2. Each worker creates only its assigned section file and individual preview main file.

3. Each worker builds only its individual preview:

   ```bash
   cd 05_deck
   mkdir -p ../06_build/latex_aux/previews/arch_XX
   xelatex -interaction=nonstopmode -halt-on-error -output-directory=../06_build/latex_aux/previews/arch_XX main_arch_XX_preview.tex
   xelatex -interaction=nonstopmode -halt-on-error -output-directory=../06_build/latex_aux/previews/arch_XX main_arch_XX_preview.tex
   cp ../06_build/latex_aux/previews/arch_XX/main_arch_XX_preview.pdf ../06_build/main_arch_XX_preview.pdf
   mkdir -p ../06_build/arch_XX_preview
   pdftoppm -png -singlefile ../06_build/main_arch_XX_preview.pdf ../06_build/arch_XX_preview/arch_XX
   ```

4. Each worker reports only:
   - changed files;
   - preview PDF path;
   - PNG preview path;
   - LaTeX errors/warnings.

5. The integrator reviews the individual slides and then updates only the registry:

   ```tex
   \input{sections/arch_04_message_passing}
   \input{sections/arch_05_readout_energy_forces}
   ```

6. The integrator rebuilds the combined architecture preview:

   ```bash
   cd 05_deck
   xelatex -interaction=nonstopmode -halt-on-error main_architecture_preview.tex
   xelatex -interaction=nonstopmode -halt-on-error main_architecture_preview.tex
   cp main_architecture_preview.pdf ../06_build/main_architecture_preview.pdf
   mkdir -p ../06_build/architecture_preview
   pdftoppm -png ../06_build/main_architecture_preview.pdf ../06_build/architecture_preview/architecture
   ```

## Current Architecture State

Registry:
- `05_deck/sections/03_methods_architecture.tex`

Currently included slides:
- `05_deck/sections/arch_01_ml_potential_task.tex`
- `05_deck/sections/arch_02_m3gnet_overview.tex`
- `05_deck/sections/arch_03_graph_featurizer.tex`

Combined preview:
- `06_build/main_architecture_preview.pdf`
- `06_build/architecture_preview/architecture-1.png`
- `06_build/architecture_preview/architecture-2.png`
- `06_build/architecture_preview/architecture-3.png`

## Rule Of Thumb

Workers create isolated slide artifacts. The integrator is the only role that changes ordering, shared registries, status files, and combined previews.
