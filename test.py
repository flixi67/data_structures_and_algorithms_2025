import pytest

# Function to be tested
def add(a, b):
    return a + b

# Test case with detailed error messages
def test_add():
    assert add(2, 3) == 5, "Adding 2 and 3 should return 5"
    assert add(-1, 1) == 0, "Adding -1 and 1 should return 0"
    assert add(-1, -1) == -2, "Adding -1 and -1 should return -2"
    assert add(0, 0) == 0, "Adding 0 and 0 should return 0"
    assert add(2.5, 1.5) == 4.0, "Adding 2.5 and 1.5 should return 4.0"
    assert add('Hello', 'World') == 'HelloWodfrld', "Adding 'Hello' and 'World' should return 'HelloWorld'"
    
test_add()