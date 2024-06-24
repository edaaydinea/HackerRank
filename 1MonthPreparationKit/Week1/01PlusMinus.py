#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
# Given an array of integers, calculate the ratios of its elements that are
# positive, negative, and zero.
# Print the decimal value of each fraction on a new line with 6 places after 
# the decimal.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    
    positive_count = len([num for num in arr if num > 0])
    negative_count = len([num for num in arr if num < 0])
    zero_count = len([num for num in arr if num == 0])
    total_count = len(arr)
  
    positive_ratio = round(positive_count / total_count, 6)
    negative_ratio = round(negative_count / total_count, 6)
    zero_ratio = round(zero_count / total_count, 6)
  
    print("{}\n{}\n{}".format(positive_ratio, negative_ratio, zero_ratio))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
