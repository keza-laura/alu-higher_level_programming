#!/usr/bin/python3
"""
This module defines a function to read
"""


def read_file(filename=""):
    """
    Reads a UTF-8 text file and prints its contents.

    Args:
        filename (str): The path to the file
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
