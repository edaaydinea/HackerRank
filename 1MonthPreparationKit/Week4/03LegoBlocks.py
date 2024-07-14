#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

# You have an infinite number of 4 types of lego blocks of sizes given as:
# - 1x1x1
# - 1x1x2
# - 1x1x3
# - 1x1x4

# Using these blocks, you want to make a wall of height n and width m. Features of the wall are:
# - The wall should not have any holes in it.
# - The wall you build should be one solid structure, so there should not be a straight vertical break across all rows of bricks.
# - The bricks must be laid horizontally.
# How many ways can the wall be built?

# Example:
# n = 2
# m = 3

#The height is 2 and the width is 3. 
# There are 9 valid permutations in all.

# Solution: 

def legoBlocks(n, m):
    MOD = 10**9 + 7
    
    row_combinations = [1, 1, 2, 4]
    
    while len(row_combinations) <= m: 
        row_combinations.append(sum(row_combinations[-4:]) % MOD)
        
    total = [pow(c, n, MOD) for c in row_combinations]
    
    unstable = [0, 0]
    
    for i in range(2, m+1):
        f = lambda j: (total[j] - unstable[j]) * total[i - j]
        result = sum(map(f, range(1, i)))
        unstable.append(result % MOD)
    
    return (total[m] - unstable[m]) % MOD
                            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
