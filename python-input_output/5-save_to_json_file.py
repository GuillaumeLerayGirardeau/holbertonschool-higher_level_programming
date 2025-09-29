#!/usr/bin/python3
"""
function that writes an object ot a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file, using a JSON representation
    """

    with open(filename, "w") as file:
        return json.dump(my_obj, file)
