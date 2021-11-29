"""Test of the Addition operation"""
from calc.operations.addition import Addition


def test_addition():
    """method calling Addition operation"""
    # Arrange
    addition = Addition.create(1, 2, 3)  # creating an addition object using 3 parameters to add
    # Act
    result = addition.get_result()
    # Assert
    assert result == 6

    # Arrange
    addition2 = Addition.create(1, 2, 3, 4, 5)  # creating an addition object using 5 parameters to add
    # Act
    result = addition2.get_result()
    # Assert
    assert result == 15
