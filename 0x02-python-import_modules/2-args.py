#!/usr/bin/python3
import sys
if len(sys.argv) > 1:
    if len(sys.argv) == 2:
        print(len(sys.argv)-1, "argument:")
        print("1: {:s}".format(sys.argv[1]))
    else:
        print(len(sys.argv)-1, "arguments:")
        for i in sys.argv[1:]:
            print("{:d}:".format(sys.argv.index(i)), "{:s}".format(i))
else:
    print("0 arguments.")
