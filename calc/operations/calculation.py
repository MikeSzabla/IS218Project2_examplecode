"""Calculation"""


class Calculation:  # pylint: disable=too-few-public-methods
    """Calculation Class"""
    def __init__(self, *args):
        """constructor setting variable amount of args into values tuple stored within the calculation"""
        self.values = args

    @classmethod
    def create(cls, *args):
        """class method create"""
        return cls(*args)
