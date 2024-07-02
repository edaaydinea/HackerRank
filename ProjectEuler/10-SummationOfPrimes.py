#!/bin/python3
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
# Find the sum of all the primes not greater than given N

# Input Format
# The first line contains an integer T i.e. number of test cases.
# The next T lines will contain an integer N.

# Output Format
# Print the value corresponding to each test case in separate lines.

# Constraints
# 1 <= T <= 10^4
# 1 <= N <= 10^6

# Sample Input
# 2
# 10
# 20

# Sample Output
# 17
# 77


import math

limit=10**6
sieve=[True]*(limit+1)
sieve[0]=sieve[1]=False

for idx in range(2,int(math.sqrt(limit)+1)):
    if sieve[idx]:
        for multiple in range(idx*idx,limit+1,idx):
            sieve[multiple]=False

cumultative_sum = [0]
current_sum=0
for i in range(1,limit+1):
    if sieve[i]:
        current_sum+=i
    cumultative_sum.append(current_sum)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(cumultative_sum[n])
    
    