#!/usr/bin/python3
"""A Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Square that inherits from Rectangle."""

    def __init__(self, size):
        """print() should print, and str() should return,
        the square description: [Square] <width>/<height>.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
