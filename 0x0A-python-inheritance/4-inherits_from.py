#!/usr/bin/python3
"""Task 4 of python - inheritance
"""


def inherits_from(obj, a_class):
    """ This returns True if the object is an instance of a class that
    inherited (directly or indirectly) the attributes of the specified
    class, otherwise it returns False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
