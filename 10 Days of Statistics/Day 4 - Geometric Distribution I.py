"""
Day 4: Geometric Distribution I

The probability that a machine produces a defective product is 1/3. What is the
probability that the 1st defect occurs that 5th item produced?

Author: Eda AYDIN

"""


def geometric(n, p):
    q = 1 - p
    return q ** (n - 1) * p


probability = list(map(int, input().split()))
p = probability[0] / probability[1]
n = int(input())

print(round(geometric(n, p), 3))
