#!/usr/bin/python3
"""
Class Student
"""


class Student:
    """
    Student Class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs == None:
            return self.__dict__
        else:
            dict_attribs = {}
            for i in attrs:
                if i in self.__dict__:
                    dict_attribs.update({i: getattr(self, i)})
            return dict_attribs
