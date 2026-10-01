"""Scheduling problems using ordering and sweep-line techniques.

Examples:
    >>> minimum_meeting_rooms([(0, 30), (5, 10), (15, 20)])
    2
    >>> employee_free_time([[(1, 3), (6, 7)], [(2, 4)], [(2, 5), (9, 12)]])
    [(5, 6), (7, 9)]
"""

from __future__ import annotations

import heapq
from collections.abc import Iterable


def minimum_meeting_rooms(meetings: Iterable[tuple[int, int]]) -> int:
    """Return the minimum concurrent rooms required."""
    ordered = sorted(meetings)
    if any(start >= end for start, end in ordered):
        raise ValueError("each meeting must have start < end")
    end_times: list[int] = []
    peak = 0
    for start, end in ordered:
        while end_times and end_times[0] <= start:
            heapq.heappop(end_times)
        heapq.heappush(end_times, end)
        peak = max(peak, len(end_times))
    return peak


def employee_free_time(
    schedules: Iterable[Iterable[tuple[int, int]]],
) -> list[tuple[int, int]]:
    """Return finite gaps when every employee is free."""
    intervals = sorted(interval for schedule in schedules for interval in schedule)
    if any(start >= end for start, end in intervals):
        raise ValueError("each interval must have start < end")
    if not intervals:
        return []
    free: list[tuple[int, int]] = []
    _, current_end = intervals[0]
    for start, end in intervals[1:]:
        if start > current_end:
            free.append((current_end, start))
        current_end = max(current_end, end)
    return free
