#!/usr/bin/python3
"""A file-writing function."""


def write_file(filename="", text=""):
    """a function that writes a string to a
    text file (UTF8) and returns the number of characters
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
