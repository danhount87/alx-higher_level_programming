#!/usr/bin/python3
# zinzinpolice

if __name__ == "__main__":
    """a program that imports functions from a file"""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
