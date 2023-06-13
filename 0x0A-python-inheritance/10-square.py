#!/usr/bin/python3
"""A class Square that inherits from Rectangle (9-rectangle.py)
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class that inherits the attributes of a class(Rectangle)
    """
    def __init__(self, size):
        """initializes the private __size attribute and validate the given
        size value using the 'integer_validator'
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
