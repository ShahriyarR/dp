import pytest
from lecture4 import climb_stairs

@pytest.mark.parametrize("input,expected", [
    (3, 3),
    (5, 8)
])
def test_climb_stairs(input, expected):
    assert climb_stairs(input) == expected

if __name__ == "__main__":
    pytest.main(["-svv"])