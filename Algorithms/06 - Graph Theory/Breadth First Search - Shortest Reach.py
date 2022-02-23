#!/bin/python3

import os


#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def getMap(edges):
    m = {}

    for i in edges:
        l1 = m.get(i[0], [])
        l1.append(i[1])
        m[i[0]] = l1

        l2 = m.get(i[1], [])
        l2.append(i[0])
        m[i[1]] = l2

    return m


def bfs(n, m, edges, s):
    # Write your code here
    edgesMap = getMap(edges)
    visited = [False] * (n + 1)
    queue = []
    values = [-1] * (n + 1)

    queue.append(s)
    visited[s] = True
    values[s] = 0
    while len(queue) > 0:
        curr = queue.pop(0)

        if curr in edgesMap:
            for i in edgesMap[curr]:
                if not visited[i]:
                    visited[i] = True
                    values[i] = values[curr] + 6
                    queue.append(i)

    ans = []
    for i in range(1, n + 1):
        if i != s:
            ans.append(values[i])

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
