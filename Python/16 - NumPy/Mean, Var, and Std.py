import numpy as np


n, m = [int(x) for x in input().strip().split()]


arr = np.array([[int(x) for x in input().strip().split()] for _ in range(n)])


print(np.mean(arr, axis = 1))
print(np.var(arr, axis = 0))
print(np.round(np.std(arr), decimals = 11))