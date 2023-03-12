#!/usr/bin/python3
# zinzinpolice

def no_c(my_string):
    '''function that removes all characters c and C from a string.'''
    cop = [x for x in my_string if x != 'c' or x != 'C']
    return ("".join(cop))
