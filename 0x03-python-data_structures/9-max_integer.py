#!/usr/bin/python3
# zinzinpolice

def max_integer(my_list=[]):
    """function that finds the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)
    a = my_list[0]
    for j in range(len(my_list)):
        if j > a:
            a = j
    return (a)
