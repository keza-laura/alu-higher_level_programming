#!/usr/bin/python3
"""
Module defining a Student class
"""


class Student:
    """Class representing a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of a Student instance"""
        return self.__dict__
