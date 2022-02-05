#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    ttl = Counter(a)
    cont = ttl.most_common(2)
    first = max(cont[0][1] + ttl[cont[0][0]+1], cont[0][1] + ttl[cont[0][0]-1])
    second = 0
    if len(cont) > 1:
        second = max(cont[1][1] + ttl[cont[1][0]+1], cont[1][1] + ttl[cont[1][0]-1])
    return max(first, second)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
