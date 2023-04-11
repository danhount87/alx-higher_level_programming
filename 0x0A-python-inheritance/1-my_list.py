#!/usr/bin/python3
"""An inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """prints the list, but sorted in ascending sort."""
        print(sorted(self))
