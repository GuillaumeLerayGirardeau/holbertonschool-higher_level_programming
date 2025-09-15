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
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif not self.__size >= 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size
