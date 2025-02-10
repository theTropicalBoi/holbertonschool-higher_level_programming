#!/usr/bin/python3
"""
Abstract class named animal using ABC package, with abstract method
called sound.
Two subclasses of animal: Dog and Cat, with abstract method called
sound
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class for Animal
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method for sound
        """
        pass


class Dog(Animal):
    """
    Subclass Dog of Animal abstract class
    """
    def sound(self):
        """
        Method for sound
        """
        return "Bark"


class Cat(Animal):
    """
    Subclass Cat of Animal abstract class
    """
    def sound(self):
        """
        Method for sound
        """
        return "Meow"
