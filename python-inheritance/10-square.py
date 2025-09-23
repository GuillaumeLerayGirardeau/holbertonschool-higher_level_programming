#!/usr/bin/python3
"""
BaseGeometry class
Rectangle class
Square class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class
    don't forget the uppercase character
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return (f"[Rectangle] {self.__size}/{self.__size}")
