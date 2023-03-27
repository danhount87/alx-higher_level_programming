#!/usr/bin/python3
#zinzinpolice

def safe_print_list(my_list=[], x=0):
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
