"""This exercise its about lists/utility functions."""

__author__ = "730480669"

def all(numbers: list[int], digit: int) -> bool:
    i: int = 0
    while i < len(numbers):
        if numbers[i] == digit:
            i = i + 1
        else:
            return False
    if i == 3:
        return True


def max(input: list[int]) -> int:
    i: int = 0
    maximum = input[0]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        while i < (len(input)):
            if input[i] > maximum:
                maximum = input[i]
            i = i + 1
    return maximum


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    i: int = 0
    valid: bool = False
    while i < len(list_one):
        if list_one[i] == list_two[i]:
            valid = True
        else:
            valid = False
            break
        i = i + 1
    return valid