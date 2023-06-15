#!/usr/bin/python3
""" Python - Input/Output Task 1"""


def write_file(filename="", text=""):
    """This opens the file in write mode with utf-8 encoding
    using the 'with' statement"""
    with open(filename, "w", encoding="utf-8") as a_file:
        a_file.write(text)
    return len(text)
