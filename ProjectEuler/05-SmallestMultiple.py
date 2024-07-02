#!/bin/python3

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?

# Input format
# First line contains t that denotes the number of test cases. This is followed by t lines, each containing an integer, n.

# Output format
# Print the required answer for each test case.

# Constraints
# 1 <= t <= 10
# 1 <= n <= 40

# Sample Input
# 2
# 3
# 10

# Sample Output
# 6
# 2520

# Explanation (step-by-step)
# 1. For n = 3, the smallest multiple that can be evenly divided by {1, 2, 3} is 6.
# 2. For n = 10, the smallest multiple that can be evenly divided by {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} is 2520.


import sys

def smallestMultiple(n):
    i = 1
    while True:
        for j in range(1, n+1):
            if i % j != 0:
                break
            if j == n:
                return i
        i += 1


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(smallestMultiple(n))
    
    