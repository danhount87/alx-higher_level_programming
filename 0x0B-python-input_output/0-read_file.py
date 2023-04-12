#!/usr/bin/python3
"""
    A text file-reading function.
"""


def read_file(filename=""):
    """
        You must use the with statement
        and prints it to stdout
    """
    with open(filename, "r", encoding='utf-8') as a_file:
        print("{}".format(a_file.read()), end="")
