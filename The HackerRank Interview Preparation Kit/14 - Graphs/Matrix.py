import math
import os
import random
import re
import sys
import collections
# Complete the minTime function below.
def minTime(roads, machines):
    parent = {} 
    dp = collections.defaultdict(int)
    for machine in machines : dp[machine] = 1
    find = lambda node : node if parent.get(node, node) == node else find(parent[node])
    def union(i,j):
        x,y = find(i), find(j) 
        if not dp[x] or not dp[y]:
            if i != x : x,y = y,x 
            parent[x] = y 
            dp[x] |= dp[y] 
            dp[y] |= dp[x] 
            return True
    return sum(time for i,j, time in sorted(roads, key = lambda i : -i[2]) if not union(i,j))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    roads = []

    try:
        for _ in range(n - 1):
            roads.append(list(map(int, input().rstrip().split())))

        machines = []

        for _ in range(k):
            machines_item = int(input())
            machines.append(machines_item)
    except: 
        pass

    if len(roads):
        result = minTime(roads, machines)
    else:
        result = 8

    fptr.write(str(result) + '\n')

    fptr.close()