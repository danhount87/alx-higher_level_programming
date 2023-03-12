#!/usr/bin/python3
# zinzinpolice

def no_c(my_string):
    '''function that removes all characters c and C from a string.'''
    copy_str = [s for s in my_string 
            if s != 'c' or s != 'C']
    return ("".join(copy_str))
