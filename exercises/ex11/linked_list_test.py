"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730480669"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at() -> None:
    """Tests if the data returned matches the value at the index given."""
    linked_list = Node(1, Node(3, Node(2, None)))
    assert value_at(linked_list, 1) == 3


def test_value_at_empty() -> None:
    """Finding a value in an empty list should raise an IndexError."""
    with pytest.raises(IndexError):
        value_at(None, 2)
    

def test_max() -> None:
    """Tests if the maximum data value of a non-empty linked list is returned."""
    linked_list = Node(1, Node(3, Node(2, None)))
    assert max(linked_list) == 3


def test_max_two() -> None:
    """Tests if the the values are are equal then one value is returned."""
    linked_list = Node(2, Node(2, Node(2, None)))
    max(linked_list) == 2


def test_linkify() -> None:
    """Tests if linkify is in order."""
    data: list[int] = [1, 2, 3, 4]
    assert linkify(data) == "1 -> 2 -> 3 -> 4 -> None"


def test_linkify_empty() -> None:
    """Makes sure if the list is empty None is retuned."""
    data: list[int] = []
    assert linkify(data) is None


def test_scale() -> None:
    """Tests if a linked list is scaled properly."""
    data: list[int] = [1, 2, 3, 4]
    assert scale(linkify(data), 2) == "2 -> 4 -> 6 -> 8 -> None"


def test_scale_value_at() -> None:
    """Tests if an individual data value is scaled properly."""
    data: list[int] = [1, 2, 3, 4]
    assert value_at(scale(linkify(data), 2), 3) == 8