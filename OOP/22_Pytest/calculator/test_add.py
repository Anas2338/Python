from add import Add

def test_add_positive_numbers():
    assert Add(2, 3) == 5

def test_add_negative_numbers():
    assert Add(-1, -1) == -2

def test_add_zero():
    assert Add(0, 5) == 5