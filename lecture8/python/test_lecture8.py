from lecture8 import paid_stair_case

def test_paid_stair_case():
    result = paid_stair_case(n=8, p=[0, 3, 2, 4, 6, 1, 1, 5, 3])
    assert result == [0, 2, 3, 5, 6, 8]