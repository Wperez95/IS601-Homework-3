"""This module contains tests for the calculator operations and calculation class"""

# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_calculation_operations(a, b, operation, expected):
    """parameters = a (decimal): 1st operand, 
    b(decimal): 2nd operand, 
    operation (function): math function to perform, 
    exptect: expected result"""
    calc = Calculation(a,b, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_repr():
    """This test verifies that the __repr__ method of a calculation instance
    returns a string that accurately represents the state of the calculation object, 
    including it's operands and operation"""
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert calc.__repr__() == expected_repr, """__repr__ method output
    doesnt match the expected string."""

def test_divide_by_zero():
    """Test division by Zero to ensure it raises ValueError"""
    #testing dividing by zero to make sure error pops up
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="cannot divide by zero"):
        calc.perform()
