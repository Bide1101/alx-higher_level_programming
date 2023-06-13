#!/usr/bin/python3
"""This function returns True or False
"""


def is_kind_of_class(obj, a_class):
    """This returns True if the object is an instance of a class that
    inherited attributes of the specified class, otherwise it returns False
    """
    return isinstance(obj, a_class)
