#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = int(0)
    if len(sys.argv) == 1:
        print (sum)
    else:
        for i in sys.argv[1:]:
            sum = sum + int(i)
        print(sum)
