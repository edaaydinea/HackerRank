#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(A):
    # Write your code here
    for i in range(n - 2):
        for x in range(n - 2):
            c = 0
            while True:
                if A[x] == min(A[x], A[x + 1], A[x + 2]):
                    break
                if c == 2:
                    return 'NO'
                i, j, k = A[x:x + 3]
                A[x:x + 3] = k, i, j

                c += 1

    return 'YES' if A[-3:] == sorted(A[-3:]) else 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
