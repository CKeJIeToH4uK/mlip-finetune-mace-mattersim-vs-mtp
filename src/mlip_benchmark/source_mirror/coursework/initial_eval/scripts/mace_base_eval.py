import numpy as np
from ase.io import read
import torch
import os
import json
from datetime import datetime
import time

from mace.calculators import MACECalculator

device = "cuda" if torch.cuda.is_available() else "cpu"

valid_path = "~/coursework/databases/test_300K.xyz"
model_path = "~/coursework/mace_models/2023-12-10-mace-128-L0_energy_epoch-249.model"
out_dir = "~/coursework/initial_eval/results/mace_base"
os.makedirs(out_dir, exist_ok=True)

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
txt_out  = os.path.join(out_dir, f"eval_{stamp}.txt")
json_out = os.path.join(out_dir, f"eval_{stamp}.json")

cfgs = read(valid_path, ":")

def eval_mace(cfgs, model_path, device="cuda"):
    calc = MACECalculator(model_paths=model_path, device=device)

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

    for a in cfgs:
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

    dE_pa = (E_pred - E_ref) / n_atoms

    rmse_E_pa = float(np.sqrt(np.mean(dE_pa ** 2)))
    mae_E_pa  = float(np.mean(np.abs(dE_pa)))

    rmse_F = float(np.sqrt(sq_f / cnt_f))
    mae_F  = float(abs_f / cnt_f)

    return {
        "model": "MACE_base_foundation",
        "model_path": model_path,
        "n_cfg": int(len(cfgs)),
        "rmse_E_per_atom_eV": rmse_E_pa,
        "mae_E_per_atom_eV": mae_E_pa,
        "rmse_F_eV_A": rmse_F,
        "mae_F_eV_A": mae_F,
        "rmse_F_meV_A": rmse_F * 1000.0,
        "mae_F_meV_A": mae_F * 1000.0,
        "time_sec_total": float(elapsed),
        "time_sec_per_cfg": float(sec_per_cfg),
    }

res = eval_mace(cfgs, model_path=model_path, device=device)

with open(txt_out, "w") as f:
    f.write("MACE base evaluation\n")
    f.write(f"timestamp = {stamp}\n")
    f.write(f"device    = {device}\n")
    if device == "cuda":
        f.write(f"gpu       = {torch.cuda.get_device_name(0)}\n")
    f.write(f"dataset   = {valid_path}\n")
    f.write(f"model     = {model_path}\n\n")

    f.write(f"n_cfg              = {res['n_cfg']}\n")
    f.write(f"RMSE(E/atom), eV   = {res['rmse_E_per_atom_eV']}\n")
    f.write(f"MAE (E/atom), eV   = {res['mae_E_per_atom_eV']}\n")
    f.write(f"RMSE(F), eV/A      = {res['rmse_F_eV_A']}\n")
    f.write(f"MAE (F), eV/A      = {res['mae_F_eV_A']}\n")
    f.write(f"RMSE(F), meV/A     = {res['rmse_F_meV_A']}\n")
    f.write(f"MAE (F), meV/A     = {res['mae_F_meV_A']}\n")
    f.write(f"time total, s      = {res['time_sec_total']}\n")
    f.write(f"time per cfg, s    = {res['time_sec_per_cfg']}\n")

with open(json_out, "w") as f:
    json.dump(res, f, indent=2)

print("Saved:")
print(" txt :", txt_out)
print(" json:", json_out)
