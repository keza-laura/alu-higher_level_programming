#!/usr/bin/python3
"""
Module defining a Student class with flexible JSON serialization
"""

class Student:
    """Class representing a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of a Student instance.

        If attrs is a list of strings, only include those attributes.
        Otherwise, include all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__
