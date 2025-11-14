#!/usr/bin/python3
"""
This module defines the Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square using Rectangle's functionality.

    Attributes:
        __size (int): The size of the square's sides (private).
    """

    def __init__(self, size):
        """
        Initializes a Square with a validated private size.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the Square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns the string representation of the Square.

        Returns:
            str: [Rectangle] <size>/<size>
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
