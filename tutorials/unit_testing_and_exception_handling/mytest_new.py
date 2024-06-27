def add(x, y):
    return x + y

# All test cases should have test_ prefix
def test_add_pass():
    assert add(1, 1) == 2
    assert add(10, 10.5) == 20.5
    
def test_add_fail():
    assert add(1, 1) == 3