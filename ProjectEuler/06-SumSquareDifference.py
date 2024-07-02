#!/bin/python3

# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385. The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025. Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640. Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Input Format
# First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.

# Output Format
# Print the required answer for each test case.

# Constraints
# 1 <= T <= 10^4
# 1 <= N <= 10^4

# Sample Input
# 2
# 3
# 10

# Sample Output
# 22
# 2640

# Explanation (step-by-step)
# For N = 3, (1 + 2 + 3)^2 - (1^2 + 2^2 + 3^2) = 36 - 14 = 22
# For N = 10, (1 + 2 + ... + 10)^2 - (1^2 + 2^2 + ... + 10^2) = 3025 - 385 = 2640

import sys

def sumSquareDifference(n):
    sumOfSquares = (n * (n + 1) * (2 * n + 1)) // 6
    squareOfSum = ((n * (n + 1)) // 2) ** 2
    return squareOfSum - sumOfSquares

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sumSquareDifference(n))