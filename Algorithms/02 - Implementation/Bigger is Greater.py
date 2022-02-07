#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    w = list(w[::-1])
    done = 0
    for i in range(1, len(w)):
        if w[i-1] > w[i]:
            for j in range(i):
                if w[j] > w[i]:
                    w[j], w[i] = w[i], w[j]
                    w = sorted(w[:i])[::-1] + w[i:]
                    return "".join(w[::-1])

    else:
        return "no answer"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
