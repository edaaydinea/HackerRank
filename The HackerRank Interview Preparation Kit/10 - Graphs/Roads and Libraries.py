#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    if c_lib < c_road:
        return c_lib * n

    cost = 0
    graph = {}
    for load in cities:
        u, v = load
        if u not in graph:
            graph.update({u : []})
        if v not in graph:
            graph.update({v : []})
        graph[u].append(v)
        graph[v].append(u)
    visited = {key: False for key in graph}

    cost = 0
    if len(graph) < n:
        cost += (n-len(graph)) * c_lib

    for node in graph:
        if not visited[node]:
            visited[node] = True
            cost += c_lib
            cost += getCostAndBuildRoad(node, graph, visited, c_road)

    return cost

def getCostAndBuildRoad(node, graph, visited, c_road):
    cost = 0
    for near_node in graph[node]:
        if not visited[near_node]:
            visited[near_node] = True
            cost += c_road
            cost += getCostAndBuildRoad(near_node, graph, visited, c_road)
    return cost
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
