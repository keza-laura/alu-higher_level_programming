#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """This class defines a square by its size."""

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size: The size of the square (no type/value verification).
        """
        self.__size = size
