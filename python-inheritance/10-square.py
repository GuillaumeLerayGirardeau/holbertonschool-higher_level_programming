#!/usr/bin/python3
"""
BaseGeometry class
Rectangle class
Square class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class
    don't forget the uppercase character
    """

    def __init__(self, size):
        self.__size = self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size
