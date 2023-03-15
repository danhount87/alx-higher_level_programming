#!/usr/bin/python3
# zinzinpolice

def search_replace(my_list, search, replace):
    '''function that replaces all occurrences
    of an element by another in a new list.'''
    yeph = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            yeph.append(replace)
        else:
            yeph.append(my_list[i])
    return yeph
