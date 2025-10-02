#!/usr/bin/python3

import pickle
"""
CustomObject class
"""


class CustomObject():
    """
    CustomObject class, contain several methods to serialize files and data
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}") + (f"\nAge: {self.age}") + (
            f"\nIs Student: {self.is_student}"
            )

    def serialize(self, filename):
        pickle.dump(self, filename)

    @classmethod
    def deserialize(cls, filename):
        return pickle.load(filename)
