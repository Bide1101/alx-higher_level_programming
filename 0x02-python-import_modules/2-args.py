#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(len(sys.argv)-1, "argument:")
        for i in sys.argv[1:]:
            print("{:d}:".format(sys.argv.index(i)), "{:s}".format(i))
    else:
        print("0 arguments.")
