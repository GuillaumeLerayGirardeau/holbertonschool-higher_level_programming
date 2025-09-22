#!/usr/bin/python3
"""
function inherits_from
"""


def inherits_from(obj, a_class):
    """
    checks if obj is a subclass of a_class
    return True if it is, else false
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
