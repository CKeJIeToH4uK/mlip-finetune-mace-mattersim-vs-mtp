# Log Snippet: repo/coursework/cross_temp_eval/slurm_logs/eval_mace_3731655.out

Original size: 1381 bytes. Full raw log not copied.

1: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/e3nn/o3/_wigner.py:10: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
2:   _Jd, _W3j_flat, _W3j_indices = torch.load(os.path.join(os.path.dirname(__file__), 'constants.pt'))
3: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/mace/calculators/mace.py:199: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
4:   torch.load(f=model_path, map_location=device)
5: WARNING:root:No dtype selected, switching to float64 to match model dtype.
6: cuequivariance or cuequivariance_torch is not available. Cuequivariance acceleration will be disabled.
9:   "model_path": "/home/brmannanov/coursework/mace_finetune/ft_300K/ft_300K.model",
10:   "dataset_path": "/home/brmannanov/coursework/databases/test_300K.xyz",
11:   "dataset_name": "test_300K",
12:   "n_cfg": 1669,
13:   "rmse_E_per_atom_eV": 0.0006788108549495291,
14:   "mae_E_per_atom_eV": 0.0005698189755214777,
15:   "rmse_F_eV_A": 0.025892802760962726,
16:   "mae_F_eV_A": 0.01856922215981723,
17:   "rmse_F_meV_A": 25.892802760962727,
18:   "mae_F_meV_A": 18.56922215981723,
19:   "time_sec_total": 64.74792664498091
20: }
