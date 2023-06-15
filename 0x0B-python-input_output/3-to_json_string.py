#!/usr/bin/python3
"""Python - Input/Output task 3"""


import json


def to_json_string(my_obj):
    """This function returns the JSON representattopn of an object
    and does not manage exceptions"""
    return json.dumps(my_obj)
