#!/usr/bin/python3
# zinzinpolice

length = len(sys.argv)
sommation = 0
if __name__ == "__main__":
    """a program that prints the result
of the addition of all arguments"""
import sys

    if length == 1:
        sommation = 0
    else:
        for i in range(1, length):
            sommation += int(sys.argv[i])
    print("{:d}".format(sommation))
