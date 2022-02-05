#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    def is_magic(s):
        for i in range(3):
            if sum(s[i*3 : i*3 + 3]) != 15:
                return False
            if sum(s[i::3]) != 15:
                return False
        if s[0] + s[4] + s[8] != 15:
            return False
        if s[2] + s[4] + s[6] != 15:
            return False
        return True
    
    
    best = None
    min_cost = 1000
    
    for p in itertools.permutations(range(1, 10)):
        cost = sum([abs(p[i] - s[i]) for i in range(len(s))])
        if cost < min_cost and is_magic(p):
            min_cost = cost
            best = p
    
    return min_cost
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.extend(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
