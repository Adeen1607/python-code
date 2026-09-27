from problem_solving.search import binary_search, lower_bound
from problem_solving.strings import group_anagrams, longest_unique_substring


def test_group_anagrams_preserves_group_members():
    groups = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert groups == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]


def test_longest_unique_substring_returns_first_longest_window():
    assert longest_unique_substring("abcabcbb") == (3, "abc")
    assert longest_unique_substring("") == (0, "")
    assert longest_unique_substring("bbbbb") == (1, "b")


def test_binary_search_and_lower_bound_handle_duplicates():
    values = [1, 2, 2, 2, 5, 8]
    assert lower_bound(values, 2) == 1
    assert lower_bound(values, 4) == 4
    assert binary_search(values, 2) == 1
    assert binary_search(values, 7) is None
