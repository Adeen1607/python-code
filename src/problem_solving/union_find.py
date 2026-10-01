"""Disjoint-set union for connectivity problems.

Examples:
    >>> count_components(5, [(0, 1), (1, 2), (3, 4)])
    2
    >>> redundant_edge([(1, 2), (1, 3), (2, 3)])
    (2, 3)
"""

from __future__ import annotations

from collections.abc import Iterable


class DisjointSet:
    """Union-find with path compression and union by size."""

    def __init__(self, size: int) -> None:
        if size < 0:
            raise ValueError("size cannot be negative")
        self.parent = list(range(size))
        self.component_size = [1] * size
        self.components = size

    def find(self, node: int) -> int:
        """Return the representative for node."""
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, left: int, right: int) -> bool:
        """Merge components and return False when already connected."""
        left_root, right_root = self.find(left), self.find(right)
        if left_root == right_root:
            return False
        if self.component_size[left_root] < self.component_size[right_root]:
            left_root, right_root = right_root, left_root
        self.parent[right_root] = left_root
        self.component_size[left_root] += self.component_size[right_root]
        self.components -= 1
        return True


def count_components(size: int, edges: Iterable[tuple[int, int]]) -> int:
    """Return the number of connected components in an undirected graph."""
    groups = DisjointSet(size)
    for left, right in edges:
        groups.union(left, right)
    return groups.components


def redundant_edge(edges: Iterable[tuple[int, int]]) -> tuple[int, int] | None:
    """Return the first edge that closes a cycle in a one-indexed graph."""
    edge_list = list(edges)
    largest = max((max(edge) for edge in edge_list), default=0)
    groups = DisjointSet(largest + 1)
    for edge in edge_list:
        if not groups.union(*edge):
            return edge
    return None
