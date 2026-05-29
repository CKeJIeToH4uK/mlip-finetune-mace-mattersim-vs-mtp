# Протокол экспериментов

Clean repo хранит не полный training environment, а curated protocol: scripts, slurm files, selected logs, verified metrics and small eval snapshots. Для каждой финальной строки сохраняется путь от summary/report table к verified CSV and raw eval snapshot where available.

Главная политика:

- финальные числа не пересчитываются в процессе сборки clean repo;
- verified CSV copied byte-for-byte where possible;
- old contexts используются только для provenance/history;
- train rows не смешиваются с held-out validation rows.
