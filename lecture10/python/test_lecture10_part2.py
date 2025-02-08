import pytest
from lecture10_part2 import num_ways


@pytest.mark.parametrize("n,expected", [
    (3, 6),
    (4, 10),
    (5, 16)
])
def test_num_ways(n, expected):
    assert num_ways(n) == expected
