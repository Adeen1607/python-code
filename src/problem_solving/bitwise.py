"""Bit-manipulation problems with constant auxiliary space.

Examples:
    >>> single_number([4, 1, 2, 1, 2])
    4
    >>> count_set_bits(0b101101)
    4
"""

from __future__ import annotations

from collections.abc import Iterable


def single_number(values: Iterable[int]) -> int:
    """Return the value appearing once when every other value appears twice."""
    result = 0
    for value in values:
        result ^= value
    return result


def count_set_bits(value: int) -> int:
    """Count 1 bits in a non-negative integer using Kernighan's algorithm."""
    if value < 0:
        raise ValueError("value must be non-negative")
    count = 0
    while value:
        value &= value - 1
        count += 1
    return count


def missing_number(values: Iterable[int]) -> int:
    """Find the missing value from distinct integers in the range 0..n."""
    numbers = list(values)
    result = len(numbers)
    for index, value in enumerate(numbers):
        result ^= index ^ value
    return result
