#!/usr/bin/python3
"""
Module text_indentation

Functions:
    text_indentation(text)
"""


def text_indentation(text):

    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    text must be a string
    return the full string, or TypeError
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    space = [".", "?", ":"]
    skip = 0
    for i in text:
        if skip == 1 and i == " ":
            skip = 0
            continue
        print(i, end="")
        if i in space:
            print("")
            print("")
            skip = 1
