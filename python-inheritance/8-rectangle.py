#!/usr/bin/python3

"""
BaseGeometry class
Rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class
    don't forget the uppercase character
    """

    def __init__(self, width, height):
        __width = super().integer_validator("width", width)
        __height = super().integer_validator("height", height)
