"""Testing the Calculator"""
from calc.calculator import Calculator
from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division


def test_get_history_length():
    """tests the the getter for history length"""
    new_calc = Calculator()
    assert new_calc.get_history_length() == 0


def test_calculator_history():
    """tests history by checking length after adding operation"""
    previous_length = Calculator.get_history_length()
    Calculator.add_number(1, 2)
    assert Calculator.get_history_length() == previous_length+1


def test_get_last_calc_result():
    """tests the get_result_of_last_calculation method"""
    Calculator.add_number(1, 2, 3)
    assert Calculator.get_result_of_last_calculation() == 6


def test_get_last_operation():
    """tests the get_last_operation method in Calculator"""
    Calculator.subtract_number(4, 1, 1, 1)
    last_operation = Calculator.get_last_operation()
    assert isinstance(last_operation, Subtraction)
    assert last_operation.get_result() == 1


def test_get_first_calc_result():
    """tests the get_result_of_first_calculation method"""
    new_calc = Calculator()
    new_calc.clear_history()
    new_calc.add_number(2, 2)
    new_calc.subtract_number(6, 3)
    assert new_calc.get_result_of_first_calculation() == 4


def test_get_first_operation():
    """tests the get_first_operation method in Calculator"""
    new_calc = Calculator()
    new_calc.add_number(2, 2)
    new_calc.subtract_number(6, 3)
    first_operation = new_calc.get_first_operation()
    assert isinstance(first_operation, Addition)
    assert first_operation.get_result() == 4


def test_clear_history():
    """tests the clear history method in Calculator"""
    Calculator.clear_history()
    assert Calculator.get_history_length() == 0


def test_remove_from_history():
    """tests the remove_from_history method in Calculator"""
    new_calc = Calculator()
    new_calc.add_number(2, 2)
    new_calc.subtract_number(6, 3)
    new_calc.multiply_number(4, 4)
    removed_operation = new_calc.remove_from_history(1)
    assert isinstance(removed_operation, Subtraction)
    assert removed_operation.get_result() == 3
    assert new_calc.get_history_length() == 2


def test_calculator_add_static():
    """Testing the Add function of the calculator"""
    Calculator.add_number(1, 1)
    last_operation = Calculator.get_last_operation()
    assert isinstance(last_operation, Addition)


def test_calculator_subtract_static():
    """Testing the subtract method of the calculator"""
    Calculator.subtract_number(1, 1)
    last_operation = Calculator.get_last_operation()
    assert isinstance(last_operation, Subtraction)


def test_calculator_multiply_static():
    """Testing the multiply method of the calculator"""
    Calculator.multiply_number(1, 1)
    last_operation = Calculator.get_last_operation()
    assert isinstance(last_operation, Multiplication)


def test_calculator_divide_static():
    """Testing the divide method of the calculator"""
    Calculator.divide_number(1, 1)
    last_operation = Calculator.get_last_operation()
    assert isinstance(last_operation, Division)
