#!/usr/bin/python3
"""A class Rectangle that inherits BaseGeometry attributes
"""


class Rectangle(BaseGeometry):
    """ Rectangle class defined as a subclass of BaseGeometry
    """
    def __init__(self, width, height):
        """initializes the private width and height attributes then
        assigns the given width and height values using the integer_validator
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """define the area of the Rectngle
        """
        return self.__width * self.__height
