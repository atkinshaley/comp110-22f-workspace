"""Exploring how variable names can representdifferent values in different scopes."""

lauren: str = "a friend"
def stranger() -> None:
    lauren: str = "a horse"
    print(lauren)