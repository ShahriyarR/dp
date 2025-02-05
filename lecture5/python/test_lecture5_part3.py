import pytest
from lecture5_part3 import climb_stairs_k_steps


@pytest.mark.parametrize("n,k,expected", [
    (3, 2, 3),
    (5, 2, 8),
    (5, 3, 13),
    # (1000000, 2, 2756670985995446685)
])
def test_climb_stairs_k_steps(n, k, expected):
    result = climb_stairs_k_steps(n, k)
    assert result == expected