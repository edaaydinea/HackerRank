#!/bin/python3

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

# Given N, Check if there exists any Pythagorean triplet for which a + b + c = N

# Find maximum possible value of abc among all such Pythagorean triplets, If there is no such Pythagorean triplet print -1.

# Input Format
# The first line contains an integer T i.e. number of test cases.
# The next T lines will contain an integer N.

# Output Format
# Print the value corresponding to each test case in separate lines.

# Constraints
# 1 <= T <= 3000
# 1 <= N <= 3000

# Sample Input
# 2
# 12
# 4

# Sample Output
# 60
# -1

# Sample Input 2
# 3
# 1000
# 1001
# 1002

# Sample Output 2
# 31875000
# -1
# -1


import sys

def find_max_pythagorean_triplet_product(n):
    max_product = -1
    # Iterate over possible values of a
    for a in range(1, n // 3):
        # b can be calculated directly from a and n
        b = (n * (n - 2 * a)) // (2 * (n - a))
        # Calculate c based on a and b
        c = n - a - b
        # Check if it's a valid Pythagorean triplet
        if a < b < c and a * a + b * b == c * c:
            max_product = max(max_product, a * b * c)
    return max_product


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(int(find_max_pythagorean_triplet_product(n)))
   