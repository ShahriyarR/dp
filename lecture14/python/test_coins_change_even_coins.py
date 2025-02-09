import pytest
from coins_change_even_coins import coin_change


@pytest.mark.parametrize(
        "n,coins,expected", [
            (4, [1, 3, 5, 10], 3), # (1, 1, 1, 1) (1, 3) (3, 1),
            (6, [1, 3, 5, 10], 8) # (1,1,1,1,1,1), (1,1,1,3), (1,1,3,1), (1,3,1,1), (3,1,1,1), (3,3), (1,5), (5,1)
        ]
)
def test_coin_change(n, coins, expected):
    assert coin_change(n, coins) == expected