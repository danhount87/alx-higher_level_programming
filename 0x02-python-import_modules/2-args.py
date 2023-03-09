#!/usr/bin/python3
# zinzinpolice

import sys

if __name__ == "__main__":
    """program that prints the number of and
    the list of its arguments."""
    karen = len(sys.argv) - 1
    if karen == 0:
        print("0 arguments.")
    elif karen == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(karen))
    for i in range(karen):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
