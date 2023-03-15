#!/usr/bin/python3
# zinzinpolice

def multiply_by_2(a_dictionary):
    '''function that returns a new dictionary
    with all values multiplied by 2'''
    gmd = {}
    for j in a_dictionary:
        gmd[j] = a_dictionary[j] * 2
    return gmd
