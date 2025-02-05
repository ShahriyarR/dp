import pytest
from lecture6_part2 import climb_stairs_k_steps_skip_red


def test_climb_stairs_k_steps_skip_red():
    result = climb_stairs_k_steps_skip_red(n=7, k=3, stairs=[False, True, False, True, True, False, False])
    assert result == 2


if __name__ == "__main__":
    pytest.main(["-svv"])