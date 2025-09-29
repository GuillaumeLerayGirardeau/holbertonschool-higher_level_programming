#!/usr-bin/python3
"""
return the dictionnary descritpion with simple data structure
"""
import json

def class_to_json(obj):
    """
    returns the dictionary description with simple data structure 
    for JSON serialization of an object
    """
    return json.dump(obj)
