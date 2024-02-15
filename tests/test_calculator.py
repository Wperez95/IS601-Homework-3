'''My Calculator Test'''
from calculator import Calculator #importing calculator folders and functions

def test_addition():
    '''Test that addition function works'''    
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test that addition function works'''    
    assert Calculator.subtract(2,2) == 0

def test_multiplication():
    '''Test that multiplication function works'''
    assert Calculator.multiply(2,2) == 4

def test_division():
    '''Test that division function works'''
    assert Calculator.divide(2,2) == 1
    # Calculator was not defined until you created
    # a class for calculator in the calculator __init__ folder
