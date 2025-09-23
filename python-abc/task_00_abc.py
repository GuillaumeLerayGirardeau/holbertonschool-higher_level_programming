#!/usr/bin/python3
"""
Abstract Class and subclasses for animal sounds
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for all animals
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Subclass of Animal
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Subclass of Animal
    """

    def sound(self):
        return "Meow"
