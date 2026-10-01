"""Linked-list transformations with explicit node ownership.

Examples:
    >>> head = from_values([1, 2, 3])
    >>> to_values(reverse_list(head))
    [3, 2, 1]
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass
class ListNode:
    """A singly linked-list node."""

    value: int
    next: ListNode | None = None


def from_values(values: Iterable[int]) -> ListNode | None:
    """Build a linked list while preserving iterable order."""
    sentinel = ListNode(0)
    tail = sentinel
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return sentinel.next


def to_values(head: ListNode | None) -> list[int]:
    """Materialize an acyclic linked list as Python values."""
    result: list[int] = []
    while head is not None:
        result.append(head.value)
        head = head.next
    return result


def reverse_list(head: ListNode | None) -> ListNode | None:
    """Reverse a list in place. Time: O(n). Space: O(1)."""
    previous = None
    current = head
    while current is not None:
        following = current.next
        current.next = previous
        previous = current
        current = following
    return previous


def has_cycle(head: ListNode | None) -> bool:
    """Detect a cycle using Floyd's tortoise-and-hare algorithm."""
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next if slow is not None else None
        fast = fast.next.next
        if slow is fast:
            return True
    return False
