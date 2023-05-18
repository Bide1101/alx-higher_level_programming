#!/usr/bin/python3
def complex_delete(new_dict, value):
    delKeys = [key for key in new_dict if new_dict[key] == value]
    for key in delKeys:
        del new_dict[key]
    return new_dict
