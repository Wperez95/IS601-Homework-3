from calculator.calculations import Calculations #this manages history of calculations
from calculator.operations import add, subtract, multiply, divide #these are the math functions
from calculator.calculation import Calculation #this represents a single calculation
from decimal import Decimal
from typing import Callable #for type hinting callable objects

class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """create and perform a calculation, then return the result"""
        calculation = Calculation.create(a, b, operation)
        #creates a calculation object using the static create method, passing in operands and operation
        Calculations.add_calculation(Calculation)
        #adds the calculation to the history managed by the calculations class
        return calculation.perform()
    
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        #will perform addition by using the _perform_operation method with the add function
        return Calculator._perform_operation(a,b, add)
    
    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        #will perform addition by using the _perform_operation method with the subtract function
        return Calculator._perform_operation(a,b, subtract)
    
    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        #will perform addition by using the _perform_operation method with the multiplication function
        return Calculator._perform_operation(a,b, multiply)
    
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        #will perform addition by using the _perform_operation method with the division function
        return Calculator._perform_operation(a,b, divide)
    