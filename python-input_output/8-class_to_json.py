#!/usr/bin/python3
"""
Function that returns the dictionary description of an object
for JSON serialization.
"""


def class_to_json(obj):

    """Returns a dictionary with simple data structure of obj"""
    return obj.__dict__
