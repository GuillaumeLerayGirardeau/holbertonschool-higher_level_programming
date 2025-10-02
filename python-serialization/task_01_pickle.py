#!/usr/bin/python3

"""
CustomObject class
"""
import pickle


class CustomObject():
    """
    CustomObject class, contain several methods to serialize files and data
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except:
            return None
