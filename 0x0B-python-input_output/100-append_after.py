#!/usr/bin/python3
""" Python - Input/Output Task 13"""


def append_after(filename="", search_string="", new_string=""):
    """Reads the content of the file"""
    with open(filename, "r") as a_file:
        lines = a_file.readlines()

    """Inserts the new string after each line"""
    with open(filename, "w") as a_file:
        for line in lines:
            a_file.write(line)
            if search_string in line:
                a_file.write(new_string)
