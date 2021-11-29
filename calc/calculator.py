""" main.py: holds the Calculator class definition"""
from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division


class Calculator:
    """ This is the Calculator class"""

    history = []

    @staticmethod
    def add_calculation_to_history(calculation):
        """adds a calculation to the end of the history"""
        Calculator.history.append(calculation)

    @staticmethod
    def get_result_of_last_calculation():
        """returns the results of the last item in the calculator history"""
        return Calculator.history[-1].get_result()

    @staticmethod
    def get_last_operation():
        """grabs the latest operation from the history"""
        return Calculator.history[-1]

    @staticmethod
    def get_result_of_first_calculation():
        """returns the results of the first item in the calculator history"""
        return Calculator.get_first_operation().get_result()

    @staticmethod
    def get_first_operation():
        """grabs the first operation from the history"""
        return Calculator.history[0]

    @staticmethod
    def get_history_length():
        """gets the length of the calculator history"""
        return len(Calculator.history)

    @staticmethod
    def clear_history():
        """clears the calculator history"""
        Calculator.history = []

    @staticmethod
    def remove_from_history(index):
        """remove an item from the calculator's history via index"""
        return Calculator.history.pop(index)

    @staticmethod
    def add_number(*args):
        """adds *args together"""
        addition = Addition.create(*args)
        Calculator.add_calculation_to_history(addition)
        return addition.get_result()

    @staticmethod
    def subtract_number(*args):
        """subtract value_b from value_a"""
        subtraction = Subtraction.create(*args)
        Calculator.add_calculation_to_history(subtraction)
        return subtraction.get_result()

    @staticmethod
    def multiply_number(*args):
        """multiply value_a and value_b"""
        multiplication = Multiplication.create(*args)
        Calculator.add_calculation_to_history(multiplication)
        return multiplication.get_result()

    @staticmethod
    def divide_number(*args):
        """divide value_a by value_b"""
        division = Division.create(*args)
        Calculator.add_calculation_to_history(division)
        return division.get_result()
