#!/usr/bin/python3
# zinzinpolice

def multiply_list_map(my_list=[], number=0):
    '''function that returns a list with all values
    multiplied by a number without using any loops.'''
    return (list(map(lambda m: m * number, my_list)))
