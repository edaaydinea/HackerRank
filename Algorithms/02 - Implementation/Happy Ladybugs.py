#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    # Write your code here
    cnt = defaultdict(int)
    for c in b:
        cnt[c] += 1

    if '_' in cnt:
        for k in cnt:
            if k == '_':
                continue
            elif cnt[k] == 1:
                return 'NO'
    else:
        prev = b[0]
        count = [1]
        for c in b[1:]:
            if prev == c:
                count[-1] += 1
            else:
                count.append(1)
                prev = c

        for i in count:
            if i < 2:
                return 'NO'

    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
