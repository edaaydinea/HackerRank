#Starting in the top left corner of 2x2 grid, and only being able to move to the right and down, there are eaxctly 6 routes to the bottom right corner.

#How many such routes are there through a NXM grid?
# As number of ways can be very large, print it module (10^9 + 7)

# Input Format
# The first line contains an integer T, the number of testcases.
# T lines follow, each containing an integer N and M.

# Constraints
# 1 <= T <= 10^3
# 1 <= N <= 500
# 1 <= M <= 500

# Output Format
# Output T lines, one for each testcase, the required answer.

# Sample Input
# 2
# 2 2
# 3 2

# Sample Output
# 6
# 10
from math import factorial as fac

for _ in range(int(input())):
    n, m = list(map(int, input().strip().split()))
    print(int(((fac(n+m)//fac(n))//(fac(m)))%((10**9) + 7)))