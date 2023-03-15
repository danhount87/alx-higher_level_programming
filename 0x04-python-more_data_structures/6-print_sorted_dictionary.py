#!/usr/bin/python3
# zinzinpolice

def print_sorted_dictionary(a_dictionary):
    '''function that prints a dictionary by ordered keys.'''
    for j in sorted(a_dictionary):
        print("{:s}: {}".format(j, a_dictionary[j]))
