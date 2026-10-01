"""Heap-based selection and streaming problems.

Examples:
    >>> top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    [1, 2]
    >>> kth_largest([3, 2, 1, 5, 6, 4], 2)
    5
"""

from __future__ import annotations

import heapq
from collections import Counter
from collections.abc import Iterable, Sequence


def top_k_frequent(values: Iterable[int], k: int) -> list[int]:
    """Return the k most frequent values with deterministic tie-breaking.

    Frequency is descending and value is ascending when counts tie.
    Time: O(n log k). Space: O(n).
    """
    if k < 0:
        raise ValueError("k cannot be negative")
    counts = Counter(values)
    if k > len(counts):
        raise ValueError("k cannot exceed the number of distinct values")
    return [value for value, _ in heapq.nsmallest(k, counts.items(), key=lambda item: (-item[1], item[0]))]


def kth_largest(values: Sequence[int], k: int) -> int:
    """Return the kth-largest value using a size-k min-heap.

    Time: O(n log k). Space: O(k).
    """
    if not 1 <= k <= len(values):
        raise ValueError("k must be between 1 and len(values)")
    heap = list(values[:k])
    heapq.heapify(heap)
    for value in values[k:]:
        if value > heap[0]:
            heapq.heapreplace(heap, value)
    return heap[0]
