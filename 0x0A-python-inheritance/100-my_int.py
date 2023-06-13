#!/usr/bin/python3
""" An implementation of the 'MyInt' class that inherits 'int' attributes
"""


class MyInt(int):
    """ 'MyInt' class is defined as a subclass of 'int'
    """
    def __eq__(self, other):
        """equality check to the superclass 'int'
	"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """inequality check to the superclass 'int'
	"""
        return not super().__ne__(other)
