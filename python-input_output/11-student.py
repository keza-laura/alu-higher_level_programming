#!/usr/bin/python3
"""
Student module
Defines a Student class with serialization/deserialization
"""


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name, and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the instance.
        If attrs is a list of strings, only include those attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replaces all attributes of the instance with those in json.
        Assumes json is a dictionary with keys matching attribute names.
        """
        for key, value in json.items():
            setattr(self, key, value)
