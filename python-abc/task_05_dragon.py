#!/usr/bin/python3
"""
Mixin classes SwimMixin and FlyMixin, each equipped with methods swim and fly
"""


class SwimMixin:
    """
    Class SwimMixin with swim() method
    """
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """
    Class FlyMixin with fly() method
    """
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """
    Class Dragon that inherits from FlyMixin and SwimMixin, and have
    a roar method
    """
    def roar(self):
        print("The dragon roars!")

draco = Dragon()
draco.swim()
draco.fly()
draco.roar()
