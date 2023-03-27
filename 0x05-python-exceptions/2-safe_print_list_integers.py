#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
"""function that prints the first x elements of a list and only integers."""
    capt = printed_ints = 0
    while True:
        try:
            if capt < x:
                print("{:d}".format(my_list[capt]), end='')
                capt += 1
                printed_ints += 1
            else:
                print()
                return printed_ints
        except (ValueError, TypeError):
            capt += 1
