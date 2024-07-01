#!/bin/python3

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below N.

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n = n - 1
    n3 = n // 3
    n5 = n // 5
    n15 = n // 15
    sum3 = 3 * n3 * (n3 + 1) // 2
    sum5 = 5 * n5 * (n5 + 1) // 2
    sum15 = 15 * n15 * (n15 + 1) // 2
    print(sum3 + sum5 - sum15)
    