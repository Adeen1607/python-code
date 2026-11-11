"""Trie prefix enumeration, ordering and deep-word regression tests."""

from problem_solving.tries import Trie


def test_prefix_results_are_sorted_and_include_exact_prefix():
    trie = Trie(["date", "dashboard", "data", "dat", "date", "dog"])
    assert trie.words_with_prefix("dat") == ["dat", "data", "date"]
    assert trie.words_with_prefix("d") == ["dashboard", "dat", "data", "date", "dog"]
    assert trie.words_with_prefix("missing") == []


def test_long_word_does_not_exceed_python_recursion_limit():
    word = "x" * 3000
    trie = Trie([word, "xylophone"])
    assert trie.words_with_prefix("x") == [word, "xylophone"]
    assert trie.contains(word)
