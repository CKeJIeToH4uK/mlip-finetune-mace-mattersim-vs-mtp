# H2O MTP clean level 20

Purpose:
Clean MTP level 20 training for H2O.

This fixes the old mismatch:
- old folder: new_datasets/water/mtp/
- old job/model names looked like mtp20
- but old train.py used MTP(..., level=16, ...)
- old metrics.json contains "level": 16

Therefore old H2O MTP numbers are MTP-16, not clean MTP-20.

New folder:
new_datasets/water/mtp_clean20_20260508/

Cluster target path:
/home/brmannanov/coursework/new_datasets/water/mtp_clean20_20260508

Input files expected on cluster:
- /home/brmannanov/coursework/new_datasets/water/convert/train_H2O.json
- /home/brmannanov/coursework/new_datasets/water/convert/valid_H2O.json

Training command:
cd /home/brmannanov/coursework/new_datasets/water/mtp_clean20_20260508
sbatch train_water_mtp20_clean.sbatch

Do not run manually on login node:
python train_water_mtp20_clean.py
mpirun -np 8 python train_water_mtp20_clean.py

Expected outputs:
- resources.txt
- exact_command.txt
- train.log
- water_mtp20_clean_<jobid>.out
- mtp20_trained.json
- metrics_20_clean.json
- metrics_20_clean.csv

Metrics required for presentation:
- energy MAE, meV/atom
- energy RMSE, meV/atom
- forces MAE, meV/Å
- forces RMSE, meV/Å

Label:
MTP-20

Old H2O MTP-16 reference:
- old folder: new_datasets/water/mtp/
- old level: level = 16
- old valid Energy MAE = 3.901132 meV/atom
- old valid Energy RMSE = 5.859228 meV/atom
- old valid Forces MAE = 333.0573 meV/Å
- old valid Forces RMSE = 480.3925 meV/Å

Do not overwrite these.
Final presentation should keep both labels:
- MTP-16
- MTP-20

Safe checks before sbatch:
bash -n train_water_mtp20_clean.sbatch
python -m py_compile train_water_mtp20_clean.py
python -m py_compile extract_metrics.py

Success checks after job finished:
grep -n '"level"' metrics_20_clean.json
grep -n "MTP level 20" train.log
python extract_metrics.py --metrics metrics_20_clean.json

Expected:
- metrics_20_clean.json contains "level": 20
- train.log contains "MTP level 20: ... parameters, 2 species"
- n_params is greater than old MTP-16 parameter count 222
- metrics_20_clean.csv has rows for train/valid energy/forces
