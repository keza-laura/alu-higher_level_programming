#!/usr/bin/python3
"""
Defines the Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using BaseGeometry's integer validator.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with validated private width and height.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the Rectangle description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
