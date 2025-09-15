#!/usr/bin/python3

"""
This module define a Square class
"""


class Square:
    """
    Define a Square class
    area: return the area of the square
    size: has a getter and a setter, define the size of the square
    position: has a getter and a setter, define the position of the square
    my_print: print the square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        error = "position must be a tuple of 2 positive integers"
        if len(value) != 2:
            raise TypeError(error)
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError(error)
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
