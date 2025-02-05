from lecture7 import paid_stair_case


def test_paid_stair_case():
    result = paid_stair_case(n=3, p=[0, 3, 2, 4])
    assert result == 6