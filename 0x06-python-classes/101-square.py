#!/usr/bin/python3
"""Defines class Square"""


class Square:
    """method that initializes a Square object"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """getter method for the size attribute"""
    @property
    def size(self):
        return self.__size

    """ setter method for the size attribute"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """getter method for the position attribute"""
    @property
    def position(self):
        return self.__position

    """a setter method for the position attribute"""
    @position.setter
    def position(self, position):
        if not isinstance(position, tuple) or \
                len(position) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    """method that calculates and returns the area of the square"""
    def area(self):
        return self.__size ** 2

    """method prints the square using #"""
    def my_print(self):
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
