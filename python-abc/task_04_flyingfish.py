#!/usr/bin/python3


class Fish:
    """
    Represents a fish with the ability to swim and a defined habitat.
    """
    def swim(self):
        """
        Prints a message indicating that the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints a message indicating the habitat of the fish.
        """
        print("The fish lives in water")


class Bird:
    """
    Represents a bird with the ability to fly and a defined habitat.
    """

    def fly(self):
        """
        Prints a message indicating that the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints a message indicating the habitat of the bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a flying fish, which inherits
    characteristics from both Fish and Bird.

    This class overrides methods from its parent
    classes to define unique behaviors
    for swimming, flying, and its habitat.
    """
    def fly(self):
        """
        Prints a message indicating that the flying fish is soaring.

        Overrides the `fly` method from the Bird class.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Prints a message indicating that the flying fish is swimming.

        Overrides the `swim` method from the Fish class.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Prints a message indicating that the flying fish lives
        both in water and in the sky.

        Overrides the `habitat` method from both Fish and Bird classes.
        """
        print("The flying fish lives both in water and the sky!")
