#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    r = 0
    rs2 = 0
    for x, y in my_list:
        r += x * y
        rs2 += y
    return (r / rs2)
