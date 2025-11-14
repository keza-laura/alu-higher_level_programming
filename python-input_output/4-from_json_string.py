#!/usr/bin/python3
"""
This module defines a function that returns a Python object represented
by a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.

    Args:
        my_str (str): JSON string representation of an object

    Returns:
        object: The deserialized Python object
    """
    return json.loads(my_str)
