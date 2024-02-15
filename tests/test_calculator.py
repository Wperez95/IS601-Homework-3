'''My test calculator'''
from calculator import add, subtract

def test_addition():
    '''test addition function works'''
    assert add(3,2) == 5

def test_subtraction():
    '''Test that subtraction function works'''
    assert subtract(3,2) == 1
    