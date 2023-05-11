#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    print("{:d} + {:d}".format(a, b), "=", "{:d}".format(add(a, b)))
    print("{:d} - {:d}".format(a, b), "=", "{:d}".format(sub(a, b)))
    print("{:d} * {:d}".format(a, b), "=", "{:d}".format(mul(a, b)))
    print("{:d} / {:d}".format(a, b), "=", "{:d}".format(div(a, b)))
