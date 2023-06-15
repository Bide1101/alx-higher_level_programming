#!/usr/bin/python3
"""Python - Input/Output Task 2"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
    and creates the file if it does not exist before
    """
    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
