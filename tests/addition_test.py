"""Test of the Addition operation"""
from calc.operations.addition import Addition


def test_addition():
    """method calling Addition operation"""
    # Arrange
    addition = Addition.create((1, 2, 3))
    # Act
    result = addition.get_result()
    # Assert
    assert result == float(6)
