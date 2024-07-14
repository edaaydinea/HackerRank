# 2^9 = 512 and the sum of its digits is 5 + 1 + 2 = 8
# What is the sum of the digits of the number 2^N?

# Input Format
# The first line contains an integer T, i.e., number of test cases.
# Next T lines will contain an integer N.

# Constraints
# 1 <= T <= 100
# 1 <= N <= 10^4

# Output Format
# Print the values corresponding to each test case.

# Sample Input
# 3
# 3
# 4
# 7

# Sample Output
# 8
# 7
# 11

print(*[(lambda n: sum([int(i) for i in str(2**n)]))(int(input())) for _ in range(int(input()))], sep='\n')