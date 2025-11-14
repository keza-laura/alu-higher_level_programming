#!/usr/bin/python3
"""
Defines the Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square using Rectangle's functionality.
    """

    def __init__(self, size):
        """
        Initializes a Square with validated private size.
        """

        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def area(self):
        """Returns the area of the Square."""
        return self.__size * self.__size

    def __str__(self):
        """Returns the Square description."""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
