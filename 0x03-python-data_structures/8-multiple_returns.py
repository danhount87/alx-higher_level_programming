#!/usr/bin/python3
# zinzinpolice

def multiple_returns(sentence):
    '''function that returns a tuple with the length of
    a string and its first character.'''
    lth = len(sentence)
    frst_char = sentence[0] if lth > 0 else "None"
    tup = lth, frst_char
    return(tup)
