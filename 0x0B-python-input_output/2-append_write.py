#!/usr/bin/python3
"""
    a file-appending function.
"""


def append_write(filename="", text=""):
    """
        a function that appends a string at the end of a
        text file (UTF8) and returns the number of characters
    """
    with open(filename, "a", encoding='utf=8') as a_file:
        return a_file.write(text)
