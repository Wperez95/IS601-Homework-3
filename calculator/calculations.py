from decimal import Decimal
from typing import Callable, List

from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        '''Add new calculation to the history'''
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        '''Retreieve entire history of calculations'''
        return cls.history
    
    @classmethod
    def clear_history(cls):
        '''Clear calculation history'''
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        '''retrives latest calculation. Returns none if there is no history'''
        if cls.history:
            return cls.history[-1]
        return None # type: ignore
    
    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        '''Finds and returns list of calculations by operation name'''
        return [calc for calc in cls.history if calc.operation.__name__== operation_name]
