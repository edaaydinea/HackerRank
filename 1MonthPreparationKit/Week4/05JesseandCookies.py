#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

# Jesse loves cookies and wants the sweetness of some cookies to be greater than value k. To do this, two cookies with the least sweetness are repeatedly mixed. This creates a special combined cookie with:
# sweetness = (1 * Least sweet cookie + 2 * 2nd least sweet cookie)
# This occurs until all the cookies have a sweetness greater than k.

# Given an array of sweetness of cookies, the sweetness of the cookies and the value of k, determine the number of operations that are needed. If it is not possible, return -1.

import heapq

def cookies(k, A):
    heapq.heapify(A)
    operations = 0
    
    while len(A) > 1 and A[0] < k:
        least_sweet = heapq.heappop(A)
        if least_sweet >= k:
            break
        second_least_sweet = heapq.heappop(A)
        new_cookie = least_sweet + 2 * second_least_sweet
        heapq.heappush(A, new_cookie)
        operations += 1
    
    if A[0] < k:
        return -1
    else:
        return operations

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
