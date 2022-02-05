#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    answer = 1
    while n!= 1:
        answer *=n
        n -=1
    print(answer)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
