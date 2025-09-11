#!/usr/bin/python3

# say_my_name: print "My name is" with a first name and a last name
def say_my_name(first_name, last_name=""):

    if not isinstance(first_name, str) or first_name == "":
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str) or last_name == "":
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")