#!/usr/bin/python3
"""
Functions to serialize and deserialize file to JSON
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize file to JSON
    """
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Deserialize file to Python Dictionnary
    """
    with open(filename) as file:
        return json.load(file)
