from add import Addition

def test_add_positive_numbers():
    assert Addition(2, 3) == 5

def test_add_negative_numbers():
    assert Addition(-1, -1) == -2

def test_add_zero():
    assert Addition(0, 5) == 5