#!/bin/python3

import sys

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome_product(n):
    largest_palindrome = 0
    # Start from the largest 3-digit number and go down
    for i in range(999, 99, -1):
        # Start from i and go down to avoid repeated calculations
        for j in range(i, 99, -1):  # Start j from i to avoid repeated calculations
            product = i * j
            if product < largest_palindrome:
                break  # No need to continue if product is already smaller
            if product < n and is_palindrome(product):
                largest_palindrome = max(largest_palindrome, product)
    return largest_palindrome


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(largest_palindrome_product(n))
    
    
    