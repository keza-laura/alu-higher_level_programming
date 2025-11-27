#!/usr/bin/python3
"""
Square module that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that defines a square using Rectangle
    """

    def __init__(self, size):
        """
        Instantiation with validated size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns string representation: [Square] size/size
        """
        return f"[Square] {self.__size}/{self.__size}"
