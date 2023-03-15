#!/usr/bin/python3
# zinzinpolice

def square_matrix_simple(matrix=[]):
    '''function that returns the number of keys in a dictionary'''
    nthn = []
    for k in matrix:
        nthn.append(list(map(lambda k: k**2, k)))
    return (nthn)
