#!/usr/bin/python3

"""
function is_same_class
"""


def is_same_class(obj, a_class):
    """
    checks if obj is an instance of the class a_class
    return true if it is, else false
    """
    return (type(obj) == a_class)
