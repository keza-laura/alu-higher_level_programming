#!/usr/bin/python3
"""
This module defines the BaseGeometry class with an unimplemented area method.
"""


class BaseGeometry:
    """
    A class representing geometric shapes.  
    Includes an area method to be implemented by subclasses.
    """

    def area(self):
        """
        Raises an exception because area is not implemented.
        """
        raise Exception("area() is not implemented")
