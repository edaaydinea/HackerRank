#!/bin/python3

import os
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

sys.setrecursionlimit(10000)


def journeyToMoon(n, astronaut):
    # Write your code here
    edgesMap = buildMap(astronaut)
    answer = n * (n - 1) // 2
    visited = [False] * (n + 1)

    for i in range(0, n):
        count = dfs(i, visited, edgesMap)
        if count > 0:
            answer -= count * (count - 1) // 2

    return answer


def dfs(s, visited, edgesMap):
    if visited[s]:
        return 0

    visited[s] = True

    count = 0
    for i in edgesMap.get(s, []):
        count += dfs(i, visited, edgesMap)

    return count + 1


def buildMap(astronaut):
    m = {}

    for i in astronaut:
        l1 = m.get(i[0], [])
        l1.append(i[1])
        m[i[0]] = l1

        l2 = m.get(i[1], [])
        l2.append(i[0])
        m[i[1]] = l2

    return m


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
