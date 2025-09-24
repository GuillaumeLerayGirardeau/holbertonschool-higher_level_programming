#!/usr/bin/python3
"""
SwimMixin and FlyMixin class, Dragon class that inherits from both mixins
"""


class SwimMixin():
    """
    Mixin Swim
    """

    def swim(self):
        print("The creature swims!")


class FlyMixin():
    """
    Mixin Fly
    """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits from fly and swim mixins
    """

    def roar(self):
        print("The dragon roars!")
