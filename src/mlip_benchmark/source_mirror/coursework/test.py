import numpy as np
from ase.io import read
from mattersim.forcefield.potential import MatterSimCalculator
import torch

path = "~/coursework/databases/test_300K.xyz"
ckpt = "~/coursework/mattersim_finetune/epoch_vs_err/finetune_result/best_model.pth"

a = read(path, 0)
E_ref = a.get_potential_energy()
N = len(a)

device = "cuda" if torch.cuda.is_available() else "cpu"
calc = MatterSimCalculator(load_path=ckpt, device=device, cutoff=5.0)
old = a.calc
a.calc = calc
E_pred = a.get_potential_energy()
a.calc = old

print("abs dE:", abs(E_pred - E_ref))
print("abs dE per atom:", abs(E_pred - E_ref)/N)
print("N atoms:", N)