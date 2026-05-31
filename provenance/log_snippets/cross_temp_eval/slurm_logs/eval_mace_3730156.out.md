# Log Snippet: repo/coursework/cross_temp_eval/slurm_logs/eval_mace_3730156.out

Original size: 1603 bytes. Full raw log not copied.

1: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/e3nn/o3/_wigner.py:10: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
2:   _Jd, _W3j_flat, _W3j_indices = torch.load(os.path.join(os.path.dirname(__file__), 'constants.pt'))
3: /home/brmannanov/.conda/envs/mace/lib/python3.11/site-packages/mace/calculators/mace.py:199: UserWarning: Environment variable TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD detected, since the`weights_only` argument was not explicitly passed to `torch.load`, forcing weights_only=False.
4:   torch.load(f=model_path, map_location=device)
5: WARNING:root:No dtype selected, switching to float64 to match model dtype.
6: cuequivariance or cuequivariance_torch is not available. Cuequivariance acceleration will be disabled.
9:   "model_path": "/home/brmannanov/coursework/mace_finetune/ft_300K/ft_300K.model",
10:   "dataset_path": "/home/brmannanov/coursework/databases/current_1200K/test_1200K.xyz",
11:   "dataset_name": "test_1200K",
12:   "n_cfg": 2139,
13:   "rmse_E_per_atom_eV": 0.0023648658927958657,
14:   "mae_E_per_atom_eV": 0.0018257299226483472,
15:   "rmse_F_eV_A": 0.12175352073610375,
16:   "mae_F_eV_A": 0.07491901081551956,
17:   "rmse_F_meV_A": 121.75352073610375,
18:   "mae_F_meV_A": 74.91901081551956,
19:   "time_sec_total": 125.0854011438787
20: }
21: slurmstepd: error: slurm_curl_request: curl_easy_perform failed to send data to 192.168.1.252:8086/write?db=slurm_jobs&rp=autogen&precision=s. Reason: Timeout was reached
22: slurmstepd: error: send data failed
