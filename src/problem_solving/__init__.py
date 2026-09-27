"""Reusable data-structure and algorithm exercises."""

from .arrays import max_subarray_sum, merge_intervals, sliding_window_max, two_sum_indices
from .dynamic_programming import coin_change_minimum, longest_increasing_subsequence
from .graphs import shortest_unweighted_path
from .search import binary_search, lower_bound
from .strings import group_anagrams, longest_unique_substring

__all__ = [
    "binary_search",
    "coin_change_minimum",
    "group_anagrams",
    "longest_increasing_subsequence",
    "longest_unique_substring",
    "lower_bound",
    "max_subarray_sum",
    "merge_intervals",
    "shortest_unweighted_path",
    "sliding_window_max",
    "two_sum_indices",
]
