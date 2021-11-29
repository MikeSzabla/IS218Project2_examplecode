"""Addition Operation"""
from calc.operations.calculation import Calculation


class Addition(Calculation):  # pylint: disable=too-few-public-methods
    """Addition Class"""

    def get_result(self):   # addition-specific method encapsulated within Addition class
        """returns all passed values added together"""
        result = self.values[0]
        for value in self.values[1:]:
            result += value
        return result
