#!/bin/python3

# By Listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. What is the Nth prime number?

# Input Format
# First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.

# Output Format
# Print the required answer for each test case.

# Constraints
# 1 <= T <= 10^3
# 1 <= N <= 10^4

# Sample Input
# 2
# 3
# 6

# Sample Output
# 5
# 13

# Explanation (step-by-step)
# First 10 prime numbers are: 2, 3, 5, 7, 11, 13, 17, 19, 23, and 29
# For N = 3, the 3rd prime number is 5
# For N = 6, the 6th prime number is 13

# Solution
# The Sieve of Eratosthenes is one of the most efficient ways to find all primes smaller than n when n is smaller than 10 million or so.


import sys

# Function to generate a list of primes using the Sieve of Eratosthenes
def generate_primes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    prime_list = [p for p in range(2, limit + 1) if is_prime[p]]
    return prime_list



# Precompute primes up to large number to covert the 10000th prime number
# 10000th prime number is 104729, but we can take a bit higher to ensure we have enough primes
primes = generate_primes(105000)


t = int(input().strip())
# Iterate through each test case
for a0 in range(t):
    n = int(input().strip())
    
    # Print the Nth prime number
    print(primes[n - 1])
    
    
    