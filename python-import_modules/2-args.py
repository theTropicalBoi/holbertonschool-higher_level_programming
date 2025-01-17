#!/usr/bin/python3
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        num_args = len(sys.argv) - 1

        if num_args == 1:
            print("{} argument:".format(num_args))
        else:
            print("{} arguments:".format(num_args))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
