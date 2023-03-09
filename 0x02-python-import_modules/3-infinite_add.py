#!/usr/bin/python3
# zinzinpolice

if __name__ == "__main__":
    """a program that prints the result
    of the addition of all arguments"""
    import sys

    sommation = 0
    for i in range(len(sys.argv) - 1):
        sommation += int(sys.argv[i + 1])
    print("{}".format(sommation))
