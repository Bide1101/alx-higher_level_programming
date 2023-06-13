#!/usr/bin/python3
""" A class function that returns True or False
"""


def is_same_class(obj, a_class):
    """ This returns True if the object is exactly an instance of
    the specified class otherwise it returns False
    """
    return type(obj) is a_class
