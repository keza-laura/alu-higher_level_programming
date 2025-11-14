#!/usr/bin/python3
"""
This module defines the Rectangle class that inherits from BaseGeometry.

Rectangle has private width and height attributes, validated using
BaseGeometry's integer_validator method.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle with private width and height.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with validated private width and height.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
