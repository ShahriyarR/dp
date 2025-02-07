import pytest
from lecture9_prob3 import max_profit


@pytest.mark.parametrize(
        "grid,expected", [
            ([
                [0, 2, 2, 1],
                [3, 1, 1, 1],
                [4, 4, 2, 0],
            ], 13),
            ([
                [0, 2, 2, 50],
                [3, 1, 1, 100],
                [4, 4, 2, 0]
            ], 154)
        ]
)
def test_max_profit(grid, expected):

    assert max_profit(grid) == expected