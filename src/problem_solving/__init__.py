"""Reusable data-structure and algorithm exercises."""

from .arrays import max_subarray_sum, merge_intervals, sliding_window_max, two_sum_indices
from .backtracking import combination_sum, unique_permutations
from .bitwise import count_set_bits, missing_number, single_number
from .dynamic_programming import coin_change_minimum, longest_increasing_subsequence
from .graphs import shortest_unweighted_path
from .greedy import can_reach_end, select_non_overlapping
from .heaps import kth_largest, top_k_frequent
from .linked_lists import ListNode, from_values, has_cycle, reverse_list, to_values
from .matrices import rotate_clockwise, spiral_order
from .scheduling import employee_free_time, minimum_meeting_rooms
from .search import binary_search, lower_bound
from .stacks import daily_temperatures, valid_brackets
from .strings import group_anagrams, longest_unique_substring
from .trees import TreeNode, is_valid_bst, level_order
from .tries import Trie
from .union_find import DisjointSet, count_components, redundant_edge

__all__ = [
    "DisjointSet",
    "ListNode",
    "TreeNode",
    "Trie",
    "binary_search",
    "can_reach_end",
    "coin_change_minimum",
    "combination_sum",
    "count_components",
    "count_set_bits",
    "daily_temperatures",
    "employee_free_time",
    "from_values",
    "group_anagrams",
    "has_cycle",
    "is_valid_bst",
    "kth_largest",
    "level_order",
    "longest_increasing_subsequence",
    "longest_unique_substring",
    "lower_bound",
    "max_subarray_sum",
    "merge_intervals",
    "minimum_meeting_rooms",
    "missing_number",
    "redundant_edge",
    "reverse_list",
    "rotate_clockwise",
    "select_non_overlapping",
    "shortest_unweighted_path",
    "single_number",
    "sliding_window_max",
    "spiral_order",
    "to_values",
    "top_k_frequent",
    "two_sum_indices",
    "unique_permutations",
    "valid_brackets",
]
