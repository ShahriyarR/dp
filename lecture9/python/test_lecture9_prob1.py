import pytest
from lecture9_prob1 import unique_paths

@pytest.mark.parametrize("m,n,expected", [
    (1, 1, 1),
    (3, 4, 10)
])
def test_unique_paths(m, n, expected):
    assert unique_paths(m, n) == expected

