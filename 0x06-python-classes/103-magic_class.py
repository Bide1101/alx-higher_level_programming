#!/usr/bin/python3
""" imports 'math' module """
import math


""" defines a class named MagicClass """


class MagicClass:
    """the private init method takes two parameters"""
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    """definition of the area method, calculates the area of the circle"""
    def area(self):
        return (self.__radius ** 2) * math.pi

    """calculates the circumference of the circle"""
    def circumference(self):
        return 2 * math.pi * self.__radius
