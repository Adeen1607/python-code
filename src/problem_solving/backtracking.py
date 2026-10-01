"""Backtracking templates with duplicate control.

Examples:
    >>> unique_permutations([1, 1, 2])
    [(1, 1, 2), (1, 2, 1), (2, 1, 1)]
    >>> combination_sum([2, 3, 6, 7], 7)
    [(2, 2, 3), (7,)]
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence


def unique_permutations(values: Sequence[int]) -> list[tuple[int, ...]]:
    """Return unique permutations in lexicographic order."""
    ordered = sorted(values)
    used = [False] * len(ordered)
    result: list[tuple[int, ...]] = []

    def visit(path: list[int]) -> None:
        if len(path) == len(ordered):
            result.append(tuple(path))
            return
        for index, value in enumerate(ordered):
            if used[index] or (index > 0 and value == ordered[index - 1] and not used[index - 1]):
                continue
            used[index] = True
            path.append(value)
            visit(path)
            path.pop()
            used[index] = False

    visit([])
    return result


def combination_sum(candidates: Iterable[int], target: int) -> list[tuple[int, ...]]:
    """Return combinations that sum to target, allowing repeated candidates."""
    if target < 0:
        raise ValueError("target cannot be negative")
    numbers = sorted(set(candidates))
    if any(number <= 0 for number in numbers):
        raise ValueError("candidates must be positive")
    result: list[tuple[int, ...]] = []

    def visit(start: int, remaining: int, path: list[int]) -> None:
        if remaining == 0:
            result.append(tuple(path))
            return
        for index in range(start, len(numbers)):
            value = numbers[index]
            if value > remaining:
                break
            path.append(value)
            visit(index, remaining - value, path)
            path.pop()

    visit(0, target, [])
    return result
