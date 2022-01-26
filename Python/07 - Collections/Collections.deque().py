"""
Author: Eda AYDIN
"""

from collections import deque

n = int(input())
D = deque()

for i in range(n):
    operation, value, *args = input().split() + [""]
    eval(f'D.{operation}({value})')

print(*D)
