"""Graph traversal problems using adjacency mappings."""

from __future__ import annotations

from collections import deque
from collections.abc import Hashable, Iterable, Mapping
from typing import TypeVar

Node = TypeVar("Node", bound=Hashable)


def shortest_unweighted_path(
    graph: Mapping[Node, Iterable[Node]], start: Node, goal: Node
) -> list[Node] | None:
    """Return one shortest path in an unweighted graph using breadth-first search.

    Time: O(V + E). Space: O(V).
    """
    if start == goal:
        return [start]

    queue: deque[Node] = deque([start])
    parent: dict[Node, Node | None] = {start: None}

    while queue:
        node = queue.popleft()
        for neighbour in graph.get(node, []):
            if neighbour in parent:
                continue
            parent[neighbour] = node
            if neighbour == goal:
                path: list[Node] = [goal]
                cursor: Node | None = goal
                while cursor != start:
                    cursor = parent[cursor]
                    if cursor is None:
                        break
                    path.append(cursor)
                return list(reversed(path))
            queue.append(neighbour)
    return None
