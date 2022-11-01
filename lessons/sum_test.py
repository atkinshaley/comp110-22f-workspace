"""Test for the sum function."""

from lessons.sum import sum


def test_sum_empty() -> None:
    xs: list[float] = []


def test_sum_single_item() -> None:
    xs: list[float] = [110.0]
    assert sum(xs) == 110.0


def test_sum_many_times() -> None:
    xs: list[float] = [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0