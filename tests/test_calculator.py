'''My Calculator Test'''
from calculator import calculator #importing calculator folders and functions

def test_addition():
    '''Test that addition function works'''    
    assert calculator.add(2,2) == 4

def test_subtraction():
    '''Test that addition function works'''    
    assert calculator.subtract(2,2) == 0

def test_multiplication():
    '''Test that multiplication function works'''
    assert calculator.multiply(2,2) == 4

def test_division():
    '''Test that division function works'''
    assert calculator.divide(2,2) == 1
