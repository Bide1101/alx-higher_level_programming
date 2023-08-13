#!/usr/bin/python3
def safe_print_division(a, b):
    """The division of 2 integers"""
    resullt = 0
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
