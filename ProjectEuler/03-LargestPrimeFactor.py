#!/bin/python3

import sys

def p_factor(n):
    if n in [1, 2, 3]:
        return True
    if n % 2==0:
        return n//2
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return n//i
        return True

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    while True:
        prime = p_factor(n)
        if prime is True:
            print(n)
            break
        else:
            n = prime