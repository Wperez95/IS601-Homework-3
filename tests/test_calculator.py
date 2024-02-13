'''My Calculator Test'''
<<<<<<< HEAD
from calculator import add, subtract, multiply, divide
=======
from calculator import calculator #importing calculator folders and functions
>>>>>>> part_2

def test_addition():
    '''Test that addition function works'''    
    assert calculator.add(2,2) == 4

def test_subtraction():
<<<<<<< HEAD
    '''Test that addition function works '''    
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test that multiplication function works'''
    assert multiply(2,2) == 4

def test_division():
    '''Test that division function works'''
    assert divide(2,2) == 1
=======
    '''Test that addition function works'''    
    assert calculator.subtract(2,2) == 0

def test_multiplication():
    '''Test that multiplication function works'''
    assert calculator.multiply(2,2) == 4

def test_division():
    '''Test that division function works'''
    assert calculator.divide(2,2) == 1
>>>>>>> part_2
