#!/bin/python3
import functools
import os


#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    found, pivot, left = 0, 0, 0
    right = functools.reduce(lambda x, y: x + y, arr[pivot + 1: len(arr) + 1], 0)
    found = (left == right)
    while (not found) and (pivot < len(arr) - 1):
        left = left + arr[pivot]
        right = right - arr[pivot + 1]
        pivot = pivot + 1
        found = (left == right)
        if found:
            break

    return "YES" if found == True else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
