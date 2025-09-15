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
        if len(value) > 2:
            raise TypeError(error)
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError(error)
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            y = 0
            while y < self.__position[1]:
                print("")
                y += 1
            for i in range(self.__size):
                x = 0
                y = 0
                while x < self.__size - 1:
                    while y < self.__position[0]:
                        print(" ", end="")
                        y += 1
                    print("#", end="")
                    x += 1
                print("#")
