#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countInversions(arr):
    x = mergeSort(arr, 0, len(arr)-1)
    return x

def merge(arr, left, middle, right):
    if(arr[middle] <= arr[middle+1]):
        return 0

    count = 0
    Left = arr[left:middle+1]
    Right = arr[middle+1:right+1]

    first = 0
    second = 0
    merged = left

    len_left  = middle+1-left
    len_right = right-middle

    while first < len_left and second < len_right:
        if Left[first] <= Right[second]:
            arr[merged] = Left[first]
            first += 1
        else:
            arr[merged] = Right[second]
            second += 1
            count += len_left - first
        merged += 1

    arr[merged: merged + len_left - first] = Left[first:]

    return count

def mergeSort(arr,left, right):
    x = 0
    if left < right:

        middle = (left+right)//2

        x = mergeSort(arr, left, middle)
        x += mergeSort(arr, middle+1, right)
        x += merge(arr, left, middle, right)

    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
