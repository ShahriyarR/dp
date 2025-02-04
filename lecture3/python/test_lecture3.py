import pytest
from lecture3 import n_sum

@pytest.mark.parametrize("input,expected", [
    (0, 0),
    (1, 1),
])
def test_edge_cases(input, expected):
    assert n_sum(input) == expected


def test_normal_case():
    assert n_sum(5) == 15


if __name__ == "__main__":
    pytest.main(["-svv"])