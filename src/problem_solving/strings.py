"""String problems focused on frequency maps and sliding windows."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable


def group_anagrams(words: Iterable[str]) -> list[list[str]]:
    """Group case-sensitive anagrams while preserving input order per group.

    Time: O(n * k log k), where k is average word length.
    """
    groups: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for word in words:
        groups[tuple(sorted(word))].append(word)
    return list(groups.values())


def longest_unique_substring(text: str) -> tuple[int, str]:
    """Return length and content of the first longest substring without repeats.

    Time: O(n). Space: O(min(n, alphabet size)).
    """
    latest: dict[str, int] = {}
    left = 0
    best_start = 0
    best_length = 0

    for right, character in enumerate(text):
        if character in latest and latest[character] >= left:
            left = latest[character] + 1
        latest[character] = right
        length = right - left + 1
        if length > best_length:
            best_start = left
            best_length = length

    return best_length, text[best_start : best_start + best_length]
