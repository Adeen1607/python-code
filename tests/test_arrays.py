import pytest

from problem_solving.arrays import (
    max_subarray_sum,
    merge_intervals,
    sliding_window_max,
    two_sum_indices,
)


def test_two_sum_returns_indices_for_valid_pair():
    assert two_sum_indices([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum_indices([3, 3], 6) == (0, 1)


def test_two_sum_returns_none_without_pair():
    assert two_sum_indices([1, 2, 3], 99) is None


def test_max_subarray_handles_mixed_and_negative_values():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray_sum([-5, -2, -8]) == -2
    with pytest.raises(ValueError):
        max_subarray_sum([])


def test_merge_intervals_combines_overlap_and_touching_ranges():
    assert merge_intervals([(1, 3), (2, 6), (8, 10), (10, 12)]) == [
        (1, 6),
        (8, 12),
    ]


def test_sliding_window_max_uses_each_complete_window():
    assert sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sliding_window_max([1, 2], 3) == []
