import pytest
from lecture9_prob2 import unique_paths_with_obstacles


@pytest.mark.parametrize(
        "grid,expected", [
            ([[0]],1),
            ([
                [0, 0, 0, 0],
                [0, 0, 1, 1],
                [0, 0, 0, 0],
            ], 3)
        ]
)
def test_unique_paths_with_obstacles(grid, expected):
    assert unique_paths_with_obstacles(grid) == expected