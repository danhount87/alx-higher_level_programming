#!/usr/bin/python3
# zinzinpolice

def print_matrix_integer(matrix=[[]]):
    '''Write a function that prints a matrix of integers.'''
    for k in range(len(matrix)):
        for m in range(len(matrix[k])):
            print("{:d}".format(matrix[k][m]), end="")
            if m != (len(matrix[k]) - 1):
                print(" ", end="")

        print("")
