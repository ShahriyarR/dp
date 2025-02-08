import pytest
from coin_change import coin_change, coin_change_with_denominations


@pytest.mark.parametrize(
        "n,expected", [
            (0, 1), # base case
            (3, 2),
            (4, 3)
        ]
)
def test_coin_change(n, expected):
    assert coin_change(n) == expected


@pytest.mark.parametrize(
        "n,coins,expected", [
            (0, [1, 3, 5, 10], 1),
            (3, [1, 3, 5, 10], 2),
            (4, [1, 3, 5, 10], 3)
        ]
)
def test_coin_change_with_denominations(n, coins, expected):
    assert coin_change_with_denominations(n, coins) == expected