#!/usr/bin/python3
# zinzinpolice

def delete_at(my_list=[], idx=0):
    """function that delete an item at a
    specific position in a list."""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
