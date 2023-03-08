#!/usr/bin/python3
# zinzinpolice

"""program that prints the ASCII alphabet, in reverse order,
alternating lowercase and uppercase"""
k = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - k)), end="")
    k = 32 if k == 0 else 0

