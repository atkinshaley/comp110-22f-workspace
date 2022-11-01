"""This exercise its about lists/utility functions and unit tests."""

__author__ = "730480669"


def only_evens(xs: list[int]) -> list[int]:
    """Returns only the even integers in the list."""
    i: int = 0
    even_list: list[int] = []
    while i < len(xs):
        if xs[i] % 2 == 0:
            even_list.append(xs[i])
        i += 1
    return even_list


def concat(one: list[int], two: list[int]) -> list[int]:
    """Returns one list consisting of list one followed by list two."""
    i: int = 0
    j: int = 0
    three: list[int] = []
    while i < len(one):
        three.append(one[i])
        i += 1
    while j < len(two):
        three.append(two[j])
        j += 1
    return three


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Returns a new list which is a segment of an original list."""
    b_list: list[int] = []
    if end > len(a_list):
        end = len(a_list)
    if start < 0:
        start = 0
    if (len(a_list) == 0) or (start > len(a_list)) or (end <= 0):
        return []
    while start < (end):
        b_list.append(a_list[start])
        start += 1
    return b_list
