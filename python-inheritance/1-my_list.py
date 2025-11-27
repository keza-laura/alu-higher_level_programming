#!/usr/bin/python3
"""
This module defines the MyList class that inherits from list.
It includes a method to print the list sorted in ascending order.
"""
class MyList(list):
    """
    MyList class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.
        Does not modify the original list.
        """
        print(sorted(self))
