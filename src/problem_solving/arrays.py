"""Array and interval problems with explicit complexity guarantees."""

from __future__ import annotations

from collections import deque
from collections.abc import Iterable, Sequence


def two_sum_indices(values: Sequence[int], target: int) -> tuple[int, int] | None:
    """Return indices of the first pair encountered that sums to target.

    Time: O(n). Space: O(n).
    """
    seen: dict[int, int] = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen.setdefault(value, index)
    return None


def max_subarray_sum(values: Sequence[int]) -> int:
    """Return the largest sum over all non-empty contiguous subarrays.

    Time: O(n). Space: O(1).
    """
    if not values:
        raise ValueError("values must contain at least one element")
    best = current = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best


def merge_intervals(intervals: Iterable[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping closed intervals.

    Time: O(n log n). Space: O(n).
    """
    ordered = sorted(intervals)
    if any(start > end for start, end in ordered):
        raise ValueError("interval start cannot exceed interval end")
    merged: list[tuple[int, int]] = []
    for start, end in ordered:
        if not merged or start > merged[-1][1]:
            merged.append((start, end))
        else:
            previous_start, previous_end = merged[-1]
            merged[-1] = (previous_start, max(previous_end, end))
    return merged


def sliding_window_max(values: Sequence[int], window: int) -> list[int]:
    """Return the maximum value in each fixed-width window.

    A monotonic deque keeps candidate indices in decreasing value order.
    Time: O(n). Space: O(window).
    """
    if window <= 0:
        raise ValueError("window must be positive")
    if window > len(values):
        return []

    candidates: deque[int] = deque()
    maxima: list[int] = []
    for index, value in enumerate(values):
        while candidates and candidates[0] <= index - window:
            candidates.popleft()
        while candidates and values[candidates[-1]] <= value:
            candidates.pop()
        candidates.append(index)
        if index >= window - 1:
            maxima.append(values[candidates[0]])
    return maxima
