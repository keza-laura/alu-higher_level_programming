#!/usr/bin/python3
"""
This module defines the BaseGeometry class.

BaseGeometry includes methods for area calculation and integer validation.
"""


class BaseGeometry:
    """
    Base class for geometric shapes.
    """

    def area(self):
        """
        Raises an exception because area is not implemented.

        Raises:
            Exception: always with message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the variable
            value (int): The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
