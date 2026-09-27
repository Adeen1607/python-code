"""Binary-search patterns for sorted sequences."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def lower_bound(values: Sequence[T], target: T) -> int:
    """Return the first index whose value is not less than target.

    Time: O(log n). Space: O(1).
    """
    left, right = 0, len(values)
    while left < right:
        middle = left + (right - left) // 2
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle
    return left


def binary_search(values: Sequence[T], target: T) -> int | None:
    """Return the first matching index, or None when target is absent."""
    index = lower_bound(values, target)
    return index if index < len(values) and values[index] == target else None
