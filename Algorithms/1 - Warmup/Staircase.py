#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(0, n):
        for j in range(0, n):
            if i + j >= n - 1:
                print("#",end="")
            else:
                print(" ",end="")
        print("\r")

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
