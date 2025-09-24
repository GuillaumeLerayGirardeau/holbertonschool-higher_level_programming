#!/usr/bin/python3
"""
class fish, bird, and flying fish that inherits from both
"""


class Fish():
    """
    Define a fish
    """

    def swim(self):
        print("The fish is swimming")
    
    def habitat(self):
        print("The fish lives in water")


class Bird():
    """
    Define a bird
    """

    def fly(self):
        print("The bird is flying")
    
    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Define a flying fish
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
