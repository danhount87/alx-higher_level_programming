#!/usr/bin/python3
# zinzinpolice

def simple_delete(my_dict, key=""):
    '''function that deletes a key in a dictionary.'''
    if key in my_dict:
        del my_dict[key]
    return (my_dict)
