#!/usr/bin/python3
"""Defines class Square"""


class Square:
    """ init method, initializes a Square object - takes 2 parameters"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """getter method - Gets the value of the private __size attribute"""
    @property
    def size(self):
        return self.__size

    """setter method - sets the value of the private __size attribute"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """getter method - gets the value of the private __position attribute"""
    @property
    def position(self):
        return self.__position

    """setter method - sets the value of the private __position attribute"""
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """calculates and returns the area of the square"""
    def area(self):
        return self.__size ** 2

    """method prints the square representation using the '#' """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
