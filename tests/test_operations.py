"""Testing Operations"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_operation_add():
    '''testing addition operation'''
    calculation = Calculation(Decimal('10'), Decimal('10'), add)
    assert calculation.perform() == Decimal('20'), "add operation failed"

def test_operation_subtract():
    '''Testing subtraction operation'''
    calculation = Calculation(Decimal('14'), Decimal('5'), subtract)
    assert calculation.perform() == Decimal('9'), "subtraction operation failed"

def test_operation_multiply():
    '''testing the multiply operation'''
    calculation = Calculation(Decimal('1'), Decimal('5'), multiply)
    assert calculation.perform() == Decimal('5'), "Multiply operation failed"

def test_operation_divide():
    '''testing the division operation'''
    calculation = Calculation(Decimal('15'), Decimal('5'), divide)
    assert calculation.perform() == Decimal('3'), "Divide operation failed"

def test_divide_by_zero():
    '''testing the divide by zero exception'''
    with pytest.raises(ValueError, match="cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
