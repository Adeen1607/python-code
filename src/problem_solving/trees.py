"""Binary-tree traversal and validation routines.

Examples:
    >>> root = TreeNode(2, TreeNode(1), TreeNode(3))
    >>> level_order(root)
    [[2], [1, 3]]
    >>> is_valid_bst(root)
    True
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass


@dataclass
class TreeNode:
    """A binary-tree node."""

    value: int
    left: TreeNode | None = None
    right: TreeNode | None = None


def level_order(root: TreeNode | None) -> list[list[int]]:
    """Return breadth-first values grouped by depth."""
    if root is None:
        return []
    queue: deque[TreeNode] = deque([root])
    levels: list[list[int]] = []
    while queue:
        level: list[int] = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        levels.append(level)
    return levels


def is_valid_bst(root: TreeNode | None) -> bool:
    """Validate strict binary-search-tree ordering in O(n) time."""
    stack: list[TreeNode] = []
    current = root
    previous: int | None = None
    while stack or current is not None:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        if previous is not None and current.value <= previous:
            return False
        previous = current.value
        current = current.right
    return True
