"""Greedy scheduling and reachability problems.

Examples:
    >>> select_non_overlapping([(1, 3), (2, 5), (4, 7), (6, 9), (8, 10)])
    [(1, 3), (4, 7), (8, 10)]
    >>> can_reach_end([2, 3, 1, 1, 4])
    True
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence


def select_non_overlapping(intervals: Iterable[tuple[int, int]]) -> list[tuple[int, int]]:
    """Select a maximum-size compatible interval set by earliest finish time."""
    ordered = sorted(intervals, key=lambda item: (item[1], item[0]))
    if any(start > end for start, end in ordered):
        raise ValueError("interval start cannot exceed interval end")
    selected: list[tuple[int, int]] = []
    last_end: int | None = None
    for start, end in ordered:
        if last_end is None or start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected


def can_reach_end(jumps: Sequence[int]) -> bool:
    """Return whether the last index is reachable. Time: O(n). Space: O(1)."""
    if any(jump < 0 for jump in jumps):
        raise ValueError("jump lengths cannot be negative")
    farthest = 0
    for index, jump in enumerate(jumps):
        if index > farthest:
            return False
        farthest = max(farthest, index + jump)
        if farthest >= len(jumps) - 1:
            return True
    return not jumps
