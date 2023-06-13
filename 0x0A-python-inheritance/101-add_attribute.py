#!/usr/bin/python3
"""This function adds a new attribute to an object if possible
"""


def add_attribute(obj, attr, value):
    """checks if a new attribute can be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
