#!/usr/bin/python3
"""
This module defines a Square class
"""


class Square():
    """This class is a Size validation for Square
    """
    def __init__(self, size=0):
        self.__size = size
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
