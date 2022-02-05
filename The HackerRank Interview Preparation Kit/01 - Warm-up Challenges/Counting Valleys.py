"""
Problem: https://www.hackerrank.com/challenges/counting-valleys/problem

Author: Eda AYDIN
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    level = 0
    total_valley = 0

    for i in path:
        if i == "U":
            level +=1
        if i == "D":
            level -=1
        if level == 0 and i == "U":
            total_valley +=1
    return total_valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    fptr.write(str(result) + '\n')
    fptr.close()
