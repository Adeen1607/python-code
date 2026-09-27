"""Dynamic-programming exercises with reconstructable reasoning."""

from __future__ import annotations

from bisect import bisect_left
from collections.abc import Iterable, Sequence


def coin_change_minimum(coins: Iterable[int], amount: int) -> int | None:
    """Return the minimum number of coins needed, or None if impossible.

    Time: O(amount * number of coins). Space: O(amount).
    """
    if amount < 0:
        raise ValueError("amount cannot be negative")
    denominations = sorted(set(coins))
    if any(coin <= 0 for coin in denominations):
        raise ValueError("coin denominations must be positive")

    unreachable = amount + 1
    best = [0] + [unreachable] * amount
    for subtotal in range(1, amount + 1):
        for coin in denominations:
            if coin > subtotal:
                break
            best[subtotal] = min(best[subtotal], best[subtotal - coin] + 1)
    return None if best[amount] == unreachable else best[amount]


def longest_increasing_subsequence(values: Sequence[int]) -> int:
    """Return the LIS length using patience sorting tails.

    Time: O(n log n). Space: O(n).
    """
    tails: list[int] = []
    for value in values:
        index = bisect_left(tails, value)
        if index == len(tails):
            tails.append(value)
        else:
            tails[index] = value
    return len(tails)
