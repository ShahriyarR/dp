import pytest
from lecture11 import fib, fib_top_down, fib_bottom_up_dp_forward, fib_bottom_up_dp_backward


@pytest.mark.parametrize(
        "n,expected",[
            (0, 0),
            (1, 1),
            (2, 1),
            (10, 55)
        ]
)
def test_fib(n, expected):
    assert fib(n) == expected



@pytest.mark.parametrize(
        "n,expected",[
            (0, 0),
            (1, 1),
            (2, 1),
            (10, 55)
        ]
)
def test_fib_top_down(n, expected):
    assert fib_top_down(n) == expected


@pytest.mark.parametrize(
        "n,expected",[
            (0, 0),
            (1, 1),
            (2, 1),
            (10, 55)
        ]
)
def test_fib_bottom_up_dp_forward(n, expected):
    assert fib_bottom_up_dp_forward(n) == expected


@pytest.mark.parametrize(
        "n,expected",[
            (0, 0),
            (1, 1),
            (2, 1),
            (10, 55)
        ]
)
def test_fib_bottom_up_dp_backward(n, expected):
    assert fib_bottom_up_dp_backward(n) == expected