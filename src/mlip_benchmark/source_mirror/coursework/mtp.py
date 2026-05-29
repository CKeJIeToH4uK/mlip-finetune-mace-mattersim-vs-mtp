#!/usr/bin/env python
# coding: utf-8

import numpy as np
from mpi4py import MPI
from mlip_4 import Cfg, CalcCfg, LossCfg, LossFunction, RadialBasisCinf, MTP, Trainer

species_order = [1, 6, 7, 8]

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

TRAIN_DB_PATH = "databases/train_300K_from_xyz.json"   # <-- поменяй под себя
VALID_DB_PATH = "databases/test_300K_from_xyz.json"   # <-- поменяй под себя


# ---------- load train ----------
train_bytes = b""
if rank == 0:
    with open(TRAIN_DB_PATH, "rb") as f:
        train_bytes = f.read()
train_bytes = comm.bcast(train_bytes, root=0)
# If the second variable in the following method is `True`, then LossCfg's in LossFunction are equally distributed
# between all the processes. If it is set to `False`, no distribution happens
# and the calculation will not speed up even if one runs this script in parallel
loss_train = LossFunction.from_json_bytes(train_bytes, True)

# ---------- load valid ----------
valid_bytes = b""
if rank == 0:
    with open(VALID_DB_PATH, "rb") as f:
        valid_bytes = f.read()
valid_bytes = comm.bcast(valid_bytes, root=0)
loss_valid = LossFunction.from_json_bytes(valid_bytes, True)

# ---------- create potential ----------
pot_bytes = b""
if rank == 0:
    rb = RadialBasisCinf(size=8, min_dist=1.0, cutoff=5.0)
    pot = MTP(rb, species_order, level=20, jit=True)
    pot.params[:] = np.random.uniform(low=-1e-3, high=1e-3, size=len(pot.params))
    pot_bytes = pot.to_json_bytes()

# !!!!!!!!!!!!!!!!!!! It is essential to make sure that potential that is being trained is the same on all the processes !!!!!!!!!!!!!
pot_bytes = comm.bcast(pot_bytes, root=0)
pot = MTP.from_json_bytes(pot_bytes)


# ---------- train ----------
trainer = Trainer(loss_train)
train_result = trainer.train(pot, max_iter_count=2000)

# ---------- errors: train ----------
loss_train.attach_pot(pot)
loss_train.calc()
train_errors = loss_train.calc_errors()

# ---------- errors: valid ----------
loss_valid.attach_pot(pot)
loss_valid.calc()
valid_errors = loss_valid.calc_errors()

if rank == 0:
    print(train_result)
    print("TRAIN:", train_errors)
    print("VALID:", valid_errors)
