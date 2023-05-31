#!/usr/bin/python3
"""Defines class Square"""


class Square:
    """init method - sets the size attribute"""
    def __init__(self, size=0):
        self.size = size

    """getter method for the size attribute"""
    @property
    def size(self):
        return self.__size

    """the setter method for the size attribute"""
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

    """method that prints the square using the # character"""
    def my_print(self):
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
