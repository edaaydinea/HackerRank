"""
Day 4: Geometric Distribution II

The probability that a machine produces a defective product is 1/3. What is the
probability that the 1st defect is found during the first 5 inspections?

Author: Eda AYDIN

"""


def geometric(n, p):
    result = 0
    q = 1 - p
    for i in range(n + 1):
        if i > 0:
            result += (q ** (i - 1) * p)

    return result


probability = list(map(int, input().split()))
p = probability[0] / probability[1]
n = int(input())

print(round(geometric(n, p), 3))
