#!/usr/bin/python3

"""
function lookup
"""


def lookup(obj):

    """
    return a list of all the methods and attributes available 
    """
    return (list(dir(obj)))
