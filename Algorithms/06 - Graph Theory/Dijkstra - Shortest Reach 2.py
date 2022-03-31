#!/bin/python3

import heapq
import os
import sys


#
# Complete the 'shortestReach' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER s


def shortestReach(n, edges, s):
    # Write your code here

    graph = []
    for i in range(n + 1):
        graph.append(set())

    for x, y, r in edges:
        graph[x].add((y, r))
        graph[y].add((x, r))

    que1 = [(0, s)]
    distance = [-1] * (n + 1)
    distance[s] = 0
    while len(que1):
        length, v = heapq.heappop(que1)
        for x, r in graph[v]:
            alt = r + distance[v]
            if alt < distance[x] or distance[x] == -1:
                distance[x] = alt
                heapq.heappush(que1, (distance[x], x))
    distance.pop(s)
    return distance[1:]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        edges = []
        for _ in range(m):
            edges.append(list(map(int, sys.stdin.readline().rstrip().split())))
        s = int(input().strip())
        result = shortestReach(n, edges, s)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
