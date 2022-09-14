#!/usr/bin/python3
"""
Create a Class Square with:
- size, position private propreties
- method of area and method of print_square
- getters & setters.
"""


class Square():
    """Square implementation
    """
    def __init__(self, size=0, position=(0, 0)):
        """Constructor of a Square with the size and position"""
        self.__size = size
        self.__position = position

    def area(self):
        """Method to get the area of the Square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Getter of the private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size private attribute"""
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
        else:
            for i in range(self.position[1]):
                print('')

            for i in range(self.size):
                print(' ' * self.position[0] + '#' * self.size)
    
    @property
    def position(self):
        """Getter of position"""
        return self.__position

    @size.setter
    def position(self, value):
        """Setter of position"""
        if type(position) != tuple or \
            len(position) != 2 or \
            not all(isinstance(el, int) for el in position) or \
                not all(el >= 0 for el in position):

            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position
