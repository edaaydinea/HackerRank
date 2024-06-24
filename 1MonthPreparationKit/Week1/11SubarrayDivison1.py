#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it. Lily decides to share a contiguous segment of the bar selected such that:
# The length of the segment matches Ron's birth month, and,
# The sum of the integers on the squares is equal to his birth day.
# Example:
# s = [1,2,1,3,2], d = 3, m = 2
# s: an array of integers, the numbers on each of the squares of chocolate
# d: an integer, Ron's birth day
# m: an integer, Ron's birth month
# Explanation:
# Lily wants to find segments summing to Ron's birth day, Ron's birth month is 2 and Ron's birth day is 3. In this case, there are two segments meeting her criteria: [1,2] and [2,1].

def birthday(s, d, m):
    # Write your code here
    # Initialize the number of ways to divide the chocolate bar
    ways = 0
    # Iterate through the chocolate bar
    for i in range(len(s)):
        # Calculate the sum of the segment starting at index i and ending at index i with length m
        segment_sum = sum(s[i:i+m])
        # If the sum of the segment is equal to Ron's birth day, increment the number of ways
        if segment_sum == d:
            ways += 1
    return ways

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
