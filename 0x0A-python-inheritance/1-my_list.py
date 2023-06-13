#!/usr/bin/python3
"""An implementation of how a class(MyList) inherits another
class(list) attributes and methods
"""


class MyList(list):
    """This class is deined as a subclass of the 'list' class
    """
    def print_sorted(self):
        """This function sorts the list in ascending order and prints it out
        """
        sorted_list = sorted(self)
        print(sorted_list)
