#!/usr/bin/python3

"""
BaseGeometry class
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
        __width = super().integer_validator("width", width)
        __height = super().integer_validator("height", height)
