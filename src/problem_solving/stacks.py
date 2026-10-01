"""Stack patterns for parsing and monotonic scans.

Examples:
    >>> valid_brackets("{[()]}")
    True
    >>> daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
    [1, 1, 4, 2, 1, 1, 0, 0]
"""

from __future__ import annotations

from collections.abc import Sequence


def valid_brackets(text: str) -> bool:
    """Return whether brackets are balanced and properly nested.

    Non-bracket characters are ignored. Time: O(n). Space: O(n).
    """
    opening = {"(": ")", "[": "]", "{": "}"}
    closing = set(opening.values())
    stack: list[str] = []
    for character in text:
        if character in opening:
            stack.append(character)
        elif character in closing:
            if not stack or opening[stack.pop()] != character:
                return False
    return not stack


def daily_temperatures(temperatures: Sequence[int]) -> list[int]:
    """Return days until a warmer temperature for every position.

    Time: O(n). Space: O(n).
    """
    waits = [0] * len(temperatures)
    unresolved: list[int] = []
    for day, temperature in enumerate(temperatures):
        while unresolved and temperatures[unresolved[-1]] < temperature:
            previous = unresolved.pop()
            waits[previous] = day - previous
        unresolved.append(day)
    return waits
