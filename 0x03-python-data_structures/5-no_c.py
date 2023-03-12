#!/usr/bin/python3
# zinzinpolice

def no_c(my_string):
    '''function that removes all characters c and C from a string.'''
    cop = my_string.translate({ord(i): None for i in 'cC'})
    return (cop)
