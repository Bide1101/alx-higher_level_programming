#!/usr/bin/python3
"""python - input/output task 0"""


def read_file(filename=""):
    """This reads a text file encoded with utf8 and prints it out to stdout"""
    with open(filename, encoding="utf-8") as afile:
        print(afile.read(), end='')
