import pytest

from problem_solving.dynamic_programming import (
    coin_change_minimum,
    longest_increasing_subsequence,
)
from problem_solving.graphs import shortest_unweighted_path


def test_shortest_unweighted_path_finds_minimum_hops():
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["F"],
        "E": ["F"],
        "F": [],
    }
    assert shortest_unweighted_path(graph, "A", "F") == ["A", "B", "D", "F"]
    assert shortest_unweighted_path(graph, "F", "A") is None
    assert shortest_unweighted_path(graph, "A", "A") == ["A"]


def test_coin_change_reports_solution_and_impossible_amount():
    assert coin_change_minimum([1, 2, 5], 11) == 3
    assert coin_change_minimum([2], 3) is None
    assert coin_change_minimum([], 0) == 0
    with pytest.raises(ValueError):
        coin_change_minimum([0, 1], 3)


def test_longest_increasing_subsequence_length():
    assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert longest_increasing_subsequence([]) == 0


def test_coin_change_short_circuits_impossible_large_amounts():
    # These inputs must not allocate a DP table proportional to the amount.
    assert coin_change_minimum([4, 6], 1_000_001) is None
    assert coin_change_minimum([100_000_000], 10_000_000) is None
    assert coin_change_minimum([], 10_000_000) is None


def test_coin_change_gcd_pruning_preserves_reachable_results():
    assert coin_change_minimum([2, 5], 11) == 4
    assert coin_change_minimum([4, 6], 12) == 2
    assert coin_change_minimum([3, 7], 0) == 0
