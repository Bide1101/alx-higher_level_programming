#!/usr/bin/python3
"""Defines class Square"""


class Square:
    def __init__(self, size=0):
        self.size = size

    """__init__ method initializes the size attribute"""
    @property
    def size(self):
        return self.__size

    """getter method - Gets the value of the size attribute"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """method that calculates and returns the area of the square"""
    def area(self):
        return self.__size ** 2
