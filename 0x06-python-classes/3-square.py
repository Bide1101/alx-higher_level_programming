#!/usr/bin/python3
"""defines a class Square"""


class Square:
    """ the init method takes 2 parameters"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """define the area method - calculates the area of the square"""
    def area(self):
        return self.__size ** 2
