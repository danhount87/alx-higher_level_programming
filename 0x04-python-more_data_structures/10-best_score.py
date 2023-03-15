#!/usr/bin/python3
# zinzinpolice

def best_score(my_dict):
    '''function that returns a key with the biggest integer value.'''
    if my_dict is None or my_dict == {}:
        return None
    biggy = max(my_dict.values())
    for kal, value in my_dict.items():
        if value is biggy:
            return kal
