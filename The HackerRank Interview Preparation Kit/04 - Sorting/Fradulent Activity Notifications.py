#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    count = 0
    count_array = [0] * 201

    for i in range(d):
        count_array[expenditure[i]] += 1

    for i in range(d, len(expenditure)):
        if expenditure[i] >= getMedianVal(count_array, d) * 2:
            count += 1
        count_array[expenditure[i - d]] -= 1
        count_array[expenditure[i]] += 1

    return count

def getMedianVal(count_arr, d):
    is_length_even = d % 2 == 0
    total_count = 0

    for i, count in enumerate(count_arr):
        total_count += count

        if is_length_even:
            if total_count == d // 2:
                for j in range(i + 1, len(count_arr)):
                    if count_arr[j] > 0:
                        return (i + j) / 2
            elif total_count > d // 2:
                return i
        else:
            if total_count >= d // 2 + 1:
                return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
