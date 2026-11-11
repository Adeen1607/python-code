"""Regression tests for zero-based union-find node validation."""

import pytest

from problem_solving.union_find import DisjointSet, count_components, redundant_edge


def test_disjoint_set_merges_components():
    groups = DisjointSet(4)
    assert groups.union(0, 1)
    assert not groups.union(1, 0)
    assert groups.components == 3
    assert count_components(4, [(0, 1), (2, 3)]) == 2
    assert redundant_edge([(1, 2), (2, 3), (1, 3)]) == (1, 3)


@pytest.mark.parametrize("invalid", [-1, 3])
def test_out_of_range_nodes_are_rejected(invalid):
    groups = DisjointSet(3)
    with pytest.raises(IndexError, match="node index out of range"):
        groups.find(invalid)
    with pytest.raises(IndexError, match="node index out of range"):
        groups.union(0, invalid)
    with pytest.raises(IndexError, match="node index out of range"):
        count_components(3, [(0, invalid)])


def test_negative_nodes_cannot_be_used_to_find_redundant_edges():
    with pytest.raises(IndexError, match="node index out of range"):
        redundant_edge([(0, -1)])
