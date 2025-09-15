#!/usr/bin/python3

"""
This module define a Square class
"""


class Square:
    """
    Define a Square class
    Square class having a private size attribute
    Don't forget the uppercase character
    """
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif not value >= 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                x = 0
                while x < self.__size - 1:
                    print("#", end="")
                    x += 1
                print("#")
