"""This file tests the functions defined in utils.py."""

__author__ = "730480669"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_return() -> None:
    """Tests if all values in even_list are even."""
    even_list: list[int] = [1, 2, 3]
    assert only_evens(even_list) == [2]


def test_only_evens_return_two() -> None:
    """Tests if all values in even_list are even."""
    even_list: list[int] = [-5, 3, 1, -2, 6, 332]
    assert only_evens(even_list) == [-2, 6, 332]


def test_only_evens_empty() -> None:
    """Tests if an empty list is returned when given an empty list."""
    even_list: list[int] = []
    assert only_evens(even_list) == []


def test_concat_return() -> None:
    """Tests if the final list is the two lists added."""
    one: list[int] = [1, 2, 3]
    two: list[int] = [7, 8, 9]
    assert concat(one, two) == [1, 2, 3, 7, 8, 9]


def test_concat_return_two() -> None:
    """Tests if the final list is the two lists added."""
    one: list[int] = [0, 3]
    two: list[int] = [-1, 2, 5, 0]
    assert concat(one, two) == [0, 3, -1, 2, 5, 0]


def test_concat_empty_list() -> None:
    """Tests if there is an empty list returned when two empty lists are given."""
    one: list[int] = []
    two: list[int] = []
    assert concat(one, two) == []


def test_sub_end_greater_len() -> None:
    """Tests subs extreme cases."""
    a_list: list[int] = [10, 20, 30, 40]
    start: int = 1
    end: int = 6
    assert sub(a_list, start, end) == [20, 30, 40]


def test_sub_return() -> None:
    """Tests if the correct segment is returned."""
    a_list: list[int] = [10, 20, 30, 40]
    start: int = 1
    end: int = 3
    assert sub(a_list, start, end) == [20, 30]


def test_sub_return_two() -> None:
    """Tests if the correct segment is returned."""
    a_list: list[int] = [10, 20, 30, 40]
    start: int = 0
    end: int = 2
    assert sub(a_list, start, end) == [10, 20]