#!/bin/python3

# Find the greatest product of K consecutive digits in the N digit number.

# Input Format
# First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N, and a number K.
# Second line of each test case will contain a N digit integer.

# Output Format
# Print the required answer for each test case.

# Constraints
# 1 <= T <= 100
# 1 <= K <= 7
# K <= N <= 1000

# Sample Input
# 2
# 10 5
# 3675356291
# 10 5
# 2709360626

# Sample Output
# 3150
# 0


# Explanation (step-by-step)
# 3675356291 => 3*6*7*5*3 = 3150
# 2709360626 => 2*7*0*9*3 = 0

import sys

def find_greatest_product(num, k):
    num = str(num)
    greatest_product = 0
    for i in range(len(num) - k):
        product = 1
        for j in range(k):
            product *= int(num[i + j])
        if product > greatest_product:
            greatest_product = product
    return greatest_product


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(find_greatest_product(num, k))