#!/usr/bin/python3

"""
BaseGeometry class
Rectangle class
"""


class BaseGeometry:
    """
    BaseGeometry class
    don't forget the double uppercase characters
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        elif not value > 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            return value


class Rectangle(BaseGeometry):
    """
    Rectangle class
    don't forget the uppercase character
    """

    def __init__(self, width, height):
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")


class Square(Rectangle):
    """
    Square class
    don't forget the uppercase character
    """

    def __init__(self, size):
        self.__size = super().integer_validator("size", size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
