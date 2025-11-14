#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance
of a class that inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a class that inherited from a_class.
    Return False if obj is a direct instance of a_class or not related at all.

    Args:
        obj: The object to inspect.
        a_class: The class to compare inheritance with.

    Returns:
        bool: True if obj inherits from a_class but is not an instance
              of a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
