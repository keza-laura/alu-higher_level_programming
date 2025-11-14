#!/usr/bin/python3
"""
This module defines a function that writes a Python object to a text file
using its JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file as JSON.

    Args:
        my_obj: The Python object to serialize
        filename (str): The path to the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
