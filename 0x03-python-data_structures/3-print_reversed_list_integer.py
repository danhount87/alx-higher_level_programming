#!/usr/bin/python3
# zinzinpolice

def print_reversed_list_integer(my_list=[]):
    '''function that prints all integers of a list, in reverse order.'''
    if isinstance(my_list, list):
        my_list.reverse()
        for k in my_list:
            print("{:d}".format(k))
