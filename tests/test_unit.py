from app.main import add, subtract

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_with_zero():
    assert add(5, 0) == 5

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2
