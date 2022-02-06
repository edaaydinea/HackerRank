#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

#
# Complete the 'countPairs' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countPairs(arr):
    power_of_2 = lambda x: x > 0 and not (x & (x - 1))
    default_dict = defaultdict(int)
    for x in arr:
        default_dict[x] += 1
    default_dict = list(default_dict.items())
    answer = 0
    for i in range(len(default_dict)):
        a, a_count = default_dict[i]
        for j in range(i, len(default_dict)):
            b, b_count = default_dict[j]
            if power_of_2(a & b):
                if a == b:
                    answer += (a_count * (a_count - 1)) // 2
                else:
                    answer += a_count * b_count
    return answer          

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = countPairs(arr)

    fptr.write(str(result) + '\n')

    fptr.close()