#!/usr/bin/python3
# zinzinpolice

def divisible_by_2(my_list=[]):
    """function that find all multiples of 2 in a list."""
    muples = []
    for j in range(len(my_list)):
        if my_list[j] % 2 == 0:
            muples.append(True)
        else:
            mples.append(False)

    return (muples)
