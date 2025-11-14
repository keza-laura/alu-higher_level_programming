#!/usr/bin/python3
"""
This module defines a function to append a string to a UTF-8 text file
and return the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a UTF-8 text file. Creates the file if it does not exist.

    Args:
        filename (str): The path to the file
        text (str): The text to append

    Returns:
        int: The number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
