#!/usr/bin/python3
"""
A Rectangle subclass Square.
"""


Rectangle = __import__('9-rectangle').Rectangle


"""
inherits from Rectangle.
"""


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ size init"""
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))