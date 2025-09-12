"""
Module Say my name

Functions:
    say_my_name(first_name, last_name="")
"""

#!/usr/bin/python3

def say_my_name(first_name, last_name=""):

    """
    Print "My name is" with first name and last name
    First name and last name must be strings
    Return the ful string, or TypeError
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")
