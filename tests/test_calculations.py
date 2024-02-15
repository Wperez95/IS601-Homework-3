'''My Calculator Test'''

from decimal import Decimal
import pytest

from calculator.calculation import Calculation
from calculator.calculations import Calculations

from calculator.operations import add, subtract

#pytest.fixture is a decorator that marks a function as a fixture
#setup mechanism used by pytest to initialize a test environment.
#here it us being used to define a fixture that prepares the test environment for calculation tests
@pytest.fixture
def setup_calculations():
    """clear history and add sample calculations for tests"""
    Calculations.clear_history()
    #add sample calculation to the history to set up a known state for testing
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('10'), add))
    Calculations.add_calculation(Calculation(Decimal('14'), Decimal('5'), subtract))

def test_add_calculation(setup_calculations):
    """Test adding a calculation to the history"""
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    # now add calculation to the history
    Calculations.add_calculation(calc)
    #assert calculation was added to the history by checking
    #if the latest calculation in the history matches what we added
    assert Calculations.get_latest() == calc, "failed to add the calculation to the history"

def test_get_history(setup_calculations):
    """Test retrieving the entire calculation history"""
    #retrieve the calculation history
    history = Calculations.get_history()
    #assert that the history contains exactly 2 calculations,
    #which should match our setup_calculations fixture above.
    assert len(history) == 2, "History does not contain the expected number of calculations"

def test_clear_history(setup_calculations):
    """test clearing the entire calculation history"""
    #clear calculation history
    Calculations.clear_history()
    #Assert that the history is empty by checking its length
    assert len(Calculations.get_history()) == 0, "History was not cleared"

def test_get_latest(setup_calculations):
    """test gettting the latest calculation from history"""
    #retreiving latest calculation from history
    latest = Calculations.get_latest()
    #assert last calculation matches expected values
    #specifically operand and operation used in last calc. in the setup_calculations fixture
    assert latest.a == Decimal('14') and latest.b == Decimal('5'), "get correct latest calculation"

def test_find_by_operation(setup_calculations):
    """Test finding calculations in the history by operation type"""
    #find all calculations with the add operation
    add_operations = Calculations.find_by_operation("add")
    #Assert that one calculation with the add operation was found
    assert len(add_operations) == 1, "Didnt get correct # of calculations with add operation"
    #find all calculations with the subtract operation
    subtract_operations = Calculations.find_by_operation("subtract")
    #Assert that one calculation with the subtract operation was found
    assert len(subtract_operations) == 1, "didnt get correct # of calcs with subtract operation"

def test_get_latest_with_empty_history():
    """Test getting the latest calculation when the history is empty"""
    #Ensure the history is empty by clearing it
    Calculations.clear_history()
    #assert that the latest calculation is none since the history is empty
    assert Calculations.get_latest() is None, "Expected None for latest calcul with empty history"
