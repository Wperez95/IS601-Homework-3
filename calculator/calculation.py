from decimal import Decimal
# importing decimal for more precise answers, good for banking and science
from typing import Callable
# importing callable from typing to specify the operation as a callable type hint
from calculator.operations import add, subtract, multiply, divide
# adding math functions from calculator/ operations folder

#defining the calculation class
class Calculation:
# below is called the constructor, has type hints for parameters and the return type (decimal)
    def __init__(self, a:Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a 
        self.b = b
        # store the operation as a callable that take 2 decimals and returns a decimal
        self.operation = operation

    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        return Calculation(a, b, operation)
    # returns a new Calculation object initialized with the provided arugument

    def perform(self) -> Decimal:
        '''Perform the stored calculation and return the result'''
    # the operation (add, substract, ect) is called with the operands (a and b) and result is returned
        return self.operation(self.a, self.b)

    #below is special method to provide a string representation of the calculation instacne
    def __repr__(self):
        '''Return a simplified strinf representation of the calculation'''
    # this method makes it easier to understand what the calculation object represents when printed or logged
    # the operation.__name__ attribute is used to get the function's name for an easier read
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
