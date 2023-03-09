#!/usr/bin/python3
# zinzinpolice

import hidden_4

if __name__ == "__main__":
    """a program that prints all the names
    defined by the compiled module"""
    for mangoes in dir(hidden_4):
        if mangoes[:2] != "__":
            print("{:s}".format(mangoes))
