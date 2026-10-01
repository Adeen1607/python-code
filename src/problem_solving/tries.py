"""Prefix-tree data structure for word and prefix lookup.

Examples:
    >>> trie = Trie(["data", "date", "dashboard"])
    >>> trie.contains("data")
    True
    >>> trie.words_with_prefix("dat")
    ['data', 'date']
"""

from __future__ import annotations

from collections.abc import Iterable


class Trie:
    """A deterministic trie supporting insertion and prefix enumeration."""

    _END = ""

    def __init__(self, words: Iterable[str] = ()) -> None:
        self._root: dict[str, dict] = {}
        for word in words:
            self.insert(word)

    def insert(self, word: str) -> None:
        """Insert one word in O(len(word)) time."""
        node = self._root
        for character in word:
            node = node.setdefault(character, {})
        node[self._END] = {}

    def contains(self, word: str) -> bool:
        """Return whether the exact word exists."""
        node = self._find_node(word)
        return node is not None and self._END in node

    def starts_with(self, prefix: str) -> bool:
        """Return whether at least one stored word starts with prefix."""
        return self._find_node(prefix) is not None

    def words_with_prefix(self, prefix: str) -> list[str]:
        """Return stored words beginning with prefix in lexical order."""
        node = self._find_node(prefix)
        if node is None:
            return []
        words: list[str] = []

        def collect(current: dict[str, dict], suffix: str) -> None:
            if self._END in current:
                words.append(prefix + suffix)
            for character in sorted(key for key in current if key != self._END):
                collect(current[character], suffix + character)

        collect(node, "")
        return words

    def _find_node(self, text: str) -> dict[str, dict] | None:
        node = self._root
        for character in text:
            if character not in node:
                return None
            node = node[character]
        return node
