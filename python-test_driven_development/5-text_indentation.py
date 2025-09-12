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
    i = 0
    while i < len(text):
        if i == 0 or skip == 1:
            skip = 0
            while text[i] == " ":
                i += 1
        print(text[i], end="")
        if text[i] in space:
            print("\n")
            skip = 1
        i += 1
