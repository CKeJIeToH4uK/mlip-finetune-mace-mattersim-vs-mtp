import numpy as np
from ase.io import read
import torch
import os
import json
import logging
import warnings
from datetime import datetime
import time

from mattersim.forcefield.potential import MatterSimCalculator

# ----------------------------
# 1) Настройки
# ----------------------------
device = "cuda"

train_path = "~/coursework/databases/train_300K.xyz"
valid_path = "~/coursework/databases/test_300K.xyz"
test_path  = None

ft_model_path = "~/coursework/mattersim_finetune/1-5million/5m/finetune_result/best_model.pth"


out_dir = "~/coursework/mattersim_finetune/1-5million/5m/best_err"
os.makedirs(out_dir, exist_ok=True)

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
txt_out  = os.path.join(out_dir, f"eval_{stamp}.txt")
json_out = os.path.join(out_dir, f"eval_{stamp}.json")
warn_log = os.path.join(out_dir, f"warnings_{stamp}.log")


warnings.filterwarnings("once", message="No PBC detected,*")

# лог варнингов в файл
logging.captureWarnings(True)
wlogger = logging.getLogger("py.warnings")
wlogger.setLevel(logging.WARNING)
fh = logging.FileHandler(warn_log)
fh.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s"))
wlogger.addHandler(fh)


# 2) Инфо о девайсе
print("device =", device)



# 3) Загрузка датасетов (ASE extxyz)
NbMo_train_cfgs_from_DFT = read(train_path, ":")
NbMo_valid_cfgs_from_DFT = read(valid_path, ":") if valid_path else None
NbMo_test_cfgs_from_DFT  = read(test_path,  ":") if test_path else None


# 4) Оценка метрик (RMSE/MAE) + тайминг
def eval_mattersim(cfgs, device="cuda", cutoff=5.0, load_path=None):
    if load_path is None:
        calc = MatterSimCalculator(device=device, cutoff=cutoff)
    else:
        calc = MatterSimCalculator(load_path=load_path, device=device, cutoff=cutoff)


    # ---- warm-up (важно для GPU/инициализаций)
    if len(cfgs) > 0:
        a0 = cfgs[0]
        old_calc = a0.calc
        a0.calc = calc
        _ = a0.get_potential_energy()
        _ = a0.get_forces()
        a0.calc = old_calc
        if device == "cuda":
            torch.cuda.synchronize()

    t0 = time.perf_counter()

    E_ref, E_pred, n_atoms = [], [], []
    sq_f, abs_f, cnt_f = 0.0, 0.0, 0

    n_no_pbc = 0
    no_pbc_idx = []

    for i, a in enumerate(cfgs):
        if not np.any(a.pbc):
            n_no_pbc += 1
            if len(no_pbc_idx) < 10:
                no_pbc_idx.append(i)

        e_ref = a.get_potential_energy()
        f_ref = a.get_forces()

        old_calc = a.calc
        a.calc = calc
        e_pred = a.get_potential_energy()
        f_pred = a.get_forces()
        a.calc = old_calc

        E_ref.append(e_ref)
        E_pred.append(e_pred)
        n_atoms.append(len(a))

        d = (f_pred - f_ref).reshape(-1)
        sq_f += float(np.dot(d, d))
        abs_f += float(np.sum(np.abs(d)))
        cnt_f += d.size

    if device == "cuda":
        torch.cuda.synchronize()
    t1 = time.perf_counter()

    elapsed = t1 - t0
    sec_per_cfg = elapsed / max(len(cfgs), 1)

    E_ref = np.array(E_ref, dtype=float)
    E_pred = np.array(E_pred, dtype=float)
    n_atoms = np.array(n_atoms, dtype=float)

    dE_pa = (E_pred - E_ref) / n_atoms  # энергия на атом

    rmse_E_pa = float(np.sqrt(np.mean(dE_pa ** 2)))
    mae_E_pa  = float(np.mean(np.abs(dE_pa)))

    rmse_F = float(np.sqrt(sq_f / cnt_f))
    mae_F  = float(abs_f / cnt_f)

    return {
        "n_cfg": int(len(cfgs)),
        "n_no_pbc": int(n_no_pbc),
        "no_pbc_first10_idx": no_pbc_idx,
        "cutoff_A": float(cutoff),

        "rmse_E_per_atom_eV": rmse_E_pa,
        "mae_E_per_atom_eV": mae_E_pa,
        "rmse_F_eV_A": rmse_F,
        "mae_F_eV_A": mae_F,
        "rmse_F_meV_A": rmse_F * 1000.0,
        "mae_F_meV_A": mae_F * 1000.0,

        "time_sec_total": float(elapsed),
        "time_sec_per_cfg": float(sec_per_cfg),
        "time_cfg_per_sec": float(1.0 / sec_per_cfg) if sec_per_cfg > 0 else None,
    }


def write_report(f, name, res):
    f.write(f"\n[{name}] n_cfg = {res['n_cfg']}\n")
    f.write(f"cutoff, Å        = {res['cutoff_A']}\n")
    f.write(f"no PBC cfgs      = {res['n_no_pbc']} (first10 idx: {res['no_pbc_first10_idx']})\n")

    f.write(f"RMSE(E/atom), eV = {res['rmse_E_per_atom_eV']}\n")
    f.write(f"MAE (E/atom), eV = {res['mae_E_per_atom_eV']}\n")
    f.write(f"RMSE(F), eV/Å    = {res['rmse_F_eV_A']}\n")
    f.write(f"MAE (F), eV/Å    = {res['mae_F_eV_A']}\n")
    f.write(f"RMSE(F), meV/Å   = {res['rmse_F_meV_A']}\n")
    f.write(f"MAE (F), meV/Å   = {res['mae_F_meV_A']}\n")

    f.write(f"time total, s    = {res['time_sec_total']}\n")
    f.write(f"time per cfg, s  = {res['time_sec_per_cfg']}\n")
    f.write(f"cfg per sec      = {res['time_cfg_per_sec']}\n")


# ----------------------------
# 5) Запуск + вывод в файлы
# ----------------------------
results = {
    "timestamp": stamp,
    "device": device,
    "gpu_name": torch.cuda.get_device_name(0) if device == "cuda" else None,
    "train_path": train_path,
    "valid_path": valid_path,
    "test_path": test_path,
    "model_load_path": ft_model_path,
    "warnings_log": warn_log,
}

with open(txt_out, "w") as f:
    f.write("MatterSim evaluation\n")
    f.write(f"timestamp = {stamp}\n")
    f.write(f"device    = {device}\n")
    if device == "cuda":
        f.write(f"gpu       = {torch.cuda.get_device_name(0)}\n")
    f.write(f"train     = {train_path}\n")
    f.write(f"valid     = {valid_path}\n")
    f.write(f"test      = {test_path}\n")
    f.write(f"warnings  = {warn_log}\n")
    f.write(f"model = {ft_model_path}\n")

    train_res = eval_mattersim(NbMo_train_cfgs_from_DFT, device=device, cutoff=5.0, load_path=ft_model_path)


    results["TRAIN"] = train_res
    write_report(f, "TRAIN", train_res)

    if NbMo_valid_cfgs_from_DFT is not None:
        valid_res = eval_mattersim(NbMo_valid_cfgs_from_DFT, device=device, cutoff=5.0, load_path=ft_model_path)
        results["VALID"] = valid_res
        write_report(f, "VALID", valid_res)

    if NbMo_test_cfgs_from_DFT is not None:
        test_res = eval_mattersim(NbMo_test_cfgs_from_DFT, device=device, cutoff=5.0, load_path=ft_model_path)
        results["TEST"] = test_res
        write_report(f, "TEST", test_res)

with open(json_out, "w") as f:
    json.dump(results, f, indent=2)

print("Saved:")
print(" txt :", txt_out)
print(" json:", json_out)
print(" warn:", warn_log)
