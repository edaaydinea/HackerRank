# !/bin/python3

import os


#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#

def cutTheTree(data, edges):
    k = {z + 1: set() for z in range(n)}
    c, l, x = 0, {1}, [0] * (n + 1)
    for a, b in edges:
        k[a].add(b)
        k[b].add(a)

    while l:
        y = set()
        for a in l:
            x[a] = c
            y |= k[a]
            for b in k[a]: k[b].remove(a)
        c, l = c + 1, y

    for z in sorted(range(1, 1 + n), key=lambda l: -x[l]):
        data[z - 1] += sum(data[b - 1] for b in k[z])
    return min(abs(data[0] - 2 * data[z]) for z in range(1, n))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
