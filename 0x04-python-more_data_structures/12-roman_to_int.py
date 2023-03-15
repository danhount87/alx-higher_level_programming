#!/usr/bin/python3
# zinzinpolice

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    man_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    man_n = 0
    for k in range(len(roman_string)):
        if k > 0 and man_d[roman_string[k]] > man_d[roman_string[k - 1]]:
            man_n += man_d[roman_string[k]] - 2 * \
                        man_d[roman_string[k - 1]]
        else:
            man_n += man_d[man_string[k]]
    return man_n
