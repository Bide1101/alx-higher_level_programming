#!/usr/bin/python3
""" Python - Input/Output Task 5"""


import json


def save_to_json_file(my_obj, filename):
    """This function writes an object to a file using a JSON representation"""
    with open(filename, "w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
