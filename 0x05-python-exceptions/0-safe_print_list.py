#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """function that prints x elements of a list."""
    sat = 0
    while True:
        try:
            if sat < x:
                print(my_list[sat], end='')
                sat += 1
            else:
                print()
                return sat
        except IndexError:
            print()
            return sat
