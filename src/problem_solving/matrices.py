"""Matrix traversal and transformation problems.

Examples:
    >>> spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [1, 2, 3, 6, 9, 8, 7, 4, 5]
    >>> rotate_clockwise([[1, 2], [3, 4]])
    [[3, 1], [4, 2]]
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def _validate_rectangular(matrix: Sequence[Sequence[T]]) -> None:
    if matrix and any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("matrix must be rectangular")


def spiral_order(matrix: Sequence[Sequence[T]]) -> list[T]:
    """Return elements in clockwise spiral order. Time: O(rows * columns)."""
    _validate_rectangular(matrix)
    if not matrix or not matrix[0]:
        return []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    result: list[T] = []
    while top <= bottom and left <= right:
        result.extend(matrix[top][left : right + 1])
        top += 1
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        if top <= bottom:
            result.extend(reversed(matrix[bottom][left : right + 1]))
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    return result


def rotate_clockwise(matrix: Sequence[Sequence[T]]) -> list[list[T]]:
    """Return a rectangular matrix rotated 90 degrees clockwise."""
    _validate_rectangular(matrix)
    return [list(reversed(column)) for column in zip(*matrix)] if matrix else []
