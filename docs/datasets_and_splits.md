# Датасеты и split labels

## organic-датасет

Основные строки: cross-temperature single-run evaluations for 300K, 600K and 1200K. MTP ensemble используется только как sanity check для 300K train/valid.

## H2O

Основные строки относятся к held-out validation split. Train-строки, если используются, не смешиваются с основными validation rows.

## MoNbTaVW

Основные строки относятся к held-out validation split. Energy-weighted MACE configuration хранится как отдельная строка от базовой MACE configuration. MTP-16 учитывается с audit caveat.
