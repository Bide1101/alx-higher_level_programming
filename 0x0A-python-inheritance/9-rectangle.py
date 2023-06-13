#!/usr/bin/python3
""" A class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
(task based on 8-rectangle.py)
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ A Rectangle class
    """
    def __init__(self, width, height):
        """initializes the private __width and __height attributes and
        validates their values using the integer_validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This defines and returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """returns a formatted string that represents the rectangle's
        description
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
