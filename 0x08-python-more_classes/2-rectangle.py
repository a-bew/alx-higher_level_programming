#!/usr/bin/python3
"""
This module defines a Rectangle Object.
"""


class Rectangle:
    """
    Rectangle class skeleton
    Args:
        width (int): width of a side in rectangle
    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        my_print(self)
    """

    def __init__(self, width=0, height=0):
        """
        Initializes square
        Attributes:
            width (int): defaults to 0 if none; don't use __size to call setter
            height (int): tuple of two positive integers
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """"
        Getter
        Return: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter
        Args:
            value: sets width to value if int and >= 0
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """"
        Getter
        Return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter
        Args:
            value: sets height to value if int and >= 0
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Calculates area of rectangle
        Returns:
            area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates perimeter of rectangle
        Returns:
            perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)