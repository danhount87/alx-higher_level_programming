#!/usr/bin/python3
"""function that adds 2 integers."""


def add_integer(a, b=98):
    """a and b must be integers or floats

    Otherwise raise a TypeError exception with the message
    a must be an integer or b must be an integer

    Returns an integer: the addition of a and b
    """
    if type(a) not in [int, float] or a is None:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or b is None:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
