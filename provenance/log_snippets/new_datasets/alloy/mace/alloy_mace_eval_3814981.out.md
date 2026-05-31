# Log Snippet: repo/coursework/new_datasets/alloy/mace/alloy_mace_eval_3814981.out

Original size: 2798 bytes. Full raw log not copied.

1: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/e3nn/o3/_wigner.py:10: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
2:   _Jd, _W3j_flat, _W3j_indices = torch.load(os.path.join(os.path.dirname(__file__), 'constants.pt'))
3: cuequivariance or cuequivariance_torch is not available. Cuequivariance acceleration will be disabled.
4: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/mace/calculators/mace.py:199: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
5:   torch.load(f=model_path, map_location=device)
6: WARNING:root:No dtype selected, switching to float64 to match model dtype.
7: {
9:   "model_path": "/home/brmannanov/coursework/new_datasets/alloy/mace/alloy_ft.model",
10:   "dataset_path": "/home/brmannanov/coursework/new_datasets/alloy/convert/valid_alloy.xyz",
11:   "dataset_name": "alloy_valid",
12:   "n_cfg": 213,
13:   "rmse_E_per_atom_eV": 0.06444756324674887,
14:   "mae_E_per_atom_eV": 0.03474367123250732,
15:   "rmse_F_eV_A": 0.12324710566119987,
16:   "mae_F_eV_A": 0.07060284896367629,
17:   "rmse_F_meV_A": 123.24710566119987,
18:   "mae_F_meV_A": 70.6028489636763,
19:   "time_sec_total": 11.573021460324526
20: }
21: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/e3nn/o3/_wigner.py:10: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
22:   _Jd, _W3j_flat, _W3j_indices = torch.load(os.path.join(os.path.dirname(__file__), 'constants.pt'))
23: cuequivariance or cuequivariance_torch is not available. Cuequivariance acceleration will be disabled.
24: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/mace/calculators/mace.py:199: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
25:   torch.load(f=model_path, map_location=device)
26: WARNING:root:No dtype selected, switching to float64 to match model dtype.
27: {
32:   "n_cfg": 1210,
33:   "rmse_E_per_atom_eV": 0.09123186361825394,
34:   "mae_E_per_atom_eV": 0.03751284493821095,
35:   "rmse_F_eV_A": 0.09760573327955008,
36:   "mae_F_eV_A": 0.06656744915990116,
37:   "rmse_F_meV_A": 97.60573327955008,
38:   "mae_F_meV_A": 66.56744915990116,
39:   "time_sec_total": 42.93754441291094
40: }
