# Log Snippet: repo/coursework/cross_temp_eval/slurm_logs/eval_mace_3730177.out

Original size: 1393 bytes. Full raw log not copied.

1: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/e3nn/o3/_wigner.py:10: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
2:   _Jd, _W3j_flat, _W3j_indices = torch.load(os.path.join(os.path.dirname(__file__), 'constants.pt'))
3: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/mace/calculators/mace.py:199: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
4:   torch.load(f=model_path, map_location=device)
5: WARNING:root:No dtype selected, switching to float64 to match model dtype.
6: cuequivariance or cuequivariance_torch is not available. Cuequivariance acceleration will be disabled.
9:   "model_path": "/home/brmannanov/coursework/mace_finetune/ft_300K/ft_300K.model",
10:   "dataset_path": "/home/brmannanov/coursework/databases/current_600K/test_600K.xyz",
11:   "dataset_name": "test_600K",
12:   "n_cfg": 2138,
13:   "rmse_E_per_atom_eV": 0.001208691745877666,
14:   "mae_E_per_atom_eV": 0.0009530024092199462,
15:   "rmse_F_eV_A": 0.049835051012961804,
16:   "mae_F_eV_A": 0.03385134744206142,
17:   "rmse_F_meV_A": 49.835051012961806,
18:   "mae_F_meV_A": 33.85134744206142,
19:   "time_sec_total": 73.91387744806707
20: }
