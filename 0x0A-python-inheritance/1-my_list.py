#!/usr/bin/python3
"""
This module defines a MyList Object.
"""

class MyList(list):
    """
    MyList class skeleton
    """
    def print_sorted(self):
        """"
        Sort
        Return: self
        """
        print(sorted(self))
