#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance
of a specified class, or an instance of a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or if obj is an instance
    of a subclass of a_class. Otherwise, return False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if isinstance(obj, a_class), otherwise False.
    """
    return isinstance(obj, a_class)
