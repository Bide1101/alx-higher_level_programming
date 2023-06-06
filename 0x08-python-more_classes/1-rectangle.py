#!/usr/bin/python3

"""
Creates an class that defines a rectangle
"""


class Rectangle:
    """
    This class defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self._Rectangle__height = height
        self._Rectangle__width = width

    @property
    def width(self):
        """
        This gets the width of the rectangle
        """
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """
        This sets the width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        """
        This gets the height of the rectangle
        """
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """
        This sets the height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value
