import pytest
from coin_change_exactly_t_coins import coin_change_exactly_t_coins


@pytest.mark.parametrize("n,t,coins,expected", [
    (0, 0, [1, 2, 3, 5], 1),
    (7, 3, [1, 2, 3, 5], 9)
])
def test_coin_change_exactly_t_coins(n, t, coins, expected):

    assert coin_change_exactly_t_coins(n, t, coins) == expected