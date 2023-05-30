#!/usr/bin/python3
def safe_print_integer(value):
    try:
        fValue = "{:d}".format(value)
        print(fValue)
        return True
    except (ValueError, TypeError):
        return False
