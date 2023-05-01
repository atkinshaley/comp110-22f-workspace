"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730480669"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test of two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None.")
    else:
        if head.next is None:
            return head.data
        else:
            return last(head.next)


def value_at(head: Optional[None], i: int) -> int:
    """Returns the data of a given Node at given index, or raises an IndexError if the index does not exist."""
    counter: int = 0
    if i < counter or counter > i:
        raise IndexError("Index is out of bounds on the list.")
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    else:
        if counter == i:
            return head.data
        else:
            if head.next is None:
                return head.data
            else:
                counter += 1
                return value_at(head.next, i - 1)


def max(head: Node) -> int:
    """Returns the max data value in a linked list."""
    m: int = head.data
    if head is None:
        raise ValueError("Cannot call max with None.")
    elif head.next is None:
        return m
    elif head.data < head.next.data:
        m = head.next.data
        return max(head.next)


def linkify(items: list[int]) -> Optional[Node]:
    """Returns a str representation of a linked list based off a given list."""
    new_node: Node = Node
    new_node.data = items[0:]
    new_node.next = linkify(items)
    if new_node.next is None:
        return Node.__str__(new_node)
    return Node.__str__(new_node)
#    if len(items) == 1:
#        return (Node.__str__(new_node))
#    if new_node.next is None:
#        return new_node
#    else:
#        i += 1
#        new_node.data = items[0:]
#        return (linkify(items))


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Resturens a scaled linked list based on given factor."""
    if head.next is None:
        return head
    else:
        return scale(head.data * factor)