#!/usr/bin/python3
"""Defines a class Rectangle with instance tracking."""


class Rectangle:
    """Represents a rectangle."""

    number_of_instances = 0  # Public class attribute

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): Rectangle width (default 0).
            height (int): Rectangle height (default 0).
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1  # Increment class counter

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value)
