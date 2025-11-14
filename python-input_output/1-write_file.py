#!/usr/bin/python3
"""
This module defines a function to write a string to a text file (UTF-8)
and return the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 text file, overwriting if it exists.

    Args:
        filename (str): The path to the file
        text (str): The text to write

    Returns:
        int: The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
