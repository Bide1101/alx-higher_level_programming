#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delKey = [key for key, value in a_dictionary.items() if value == value]
    for key in delKey:
        del a_dictionary[key]
    return a_dictionary
