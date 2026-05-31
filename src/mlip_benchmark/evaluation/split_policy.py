"""Split-label policy used by the clean repo validators."""

VALIDATION_SYSTEMS = {"H2O", "MoNbTaVW"}
ORGANIC_ALLOWED_SPLIT_PREFIXES = ("test_", "train", "valid")


def is_validation_system(system: str) -> bool:
    return system in VALIDATION_SYSTEMS
