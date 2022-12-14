#!/usr/bin/python3
"""
This module defines a Square class

Its implements value and type checks for its attributes
"""


class Square():
    """Square implementation
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """prints a square  with the corresponding size
        """
        if (self.__size == 0):
            print('')

        for i in range(self.__size):
            print("#" * self.__size)
