#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delKeys = [key for key in a_dictionary if a_dictionary[key] == value]
    for key in delKeys:
        del a_dictionary[key]
    return a_dctionary
