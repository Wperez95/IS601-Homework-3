from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide

class calculator:
    @staticmethod
    def add(a,b):
        calculation = Calculations(a,b,add) # This function is coming from thr operations folder
        return calculation.get_result()
    @staticmethod
    def subtract (a,b):
        calculation = Calculations(a,b,subtract)
        return calculation.get_result()
    
    @staticmethod
    def multiply(a,b):
        calculation = Calculations(a,b,multiply)
        return calculation.get_result()
    
    @staticmethod
    def divide(a,b):
        calculation = Calculations(a,b,divide)
        return calculation.get_result()
    
