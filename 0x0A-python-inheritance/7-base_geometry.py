#!/usr/bin/python3
""" A class BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry:
    """ A class BaseGeometry
    """
    def area(self):
        """defines an area of geometry but raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if the value is an integer using the isinstance function
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
