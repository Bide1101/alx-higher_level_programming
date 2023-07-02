#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiDict = {}
    for key, val in a_dictionary.items():
        multiDict[key] = val * 2
    return multiDict
