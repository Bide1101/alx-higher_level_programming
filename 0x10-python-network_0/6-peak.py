#!/usr/bin/python3
"""
This finds the 'peak' in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    This function is used to find the 'peak', using the lowest complexity
    """
    try:
        peakNum = max(list_of_integers)
        return peakNum
    except ValueError:
        return None
