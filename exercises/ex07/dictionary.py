"""Functions for ex07."""

__author__ = "730480669"


def invert(dict_one: dict[str, str]) -> dict[str, str]:
    dict_two = {}
    dict_two = dict((dict_two[key], key) for key in dict_one)

def favorite_color(name_color: dict[str, str]) -> str:
    i: int = 0
    points: int = 0
    for value in name_color:
        if value[i] == value:
            points += 1
        i += 1
    return 