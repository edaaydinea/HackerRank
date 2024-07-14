# Work out the first ten digits of the sum of N 50-digit numbers.

# Input Format
# First line contains N, next N lines contain a 50 digit number each.

# Constraints
# 1 <= N <= 10^3

# Output Format
# Print only first 10 digit of the final sum

print(str(sum([int(input()) for _ in range(int(input()))]))[:10])