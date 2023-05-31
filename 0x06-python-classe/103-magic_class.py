#!/usr/bin/python3
""" imports 'math' module """
import math


""" defines a class named MagicClass """


class MagicClass:
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
