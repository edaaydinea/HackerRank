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

class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def add_city(self, u):
        if u not in self.adj_list:
            self.adj_list[u] = []

    def dfs(self, start, visited):
        visited.add(start)
        print("Visitando cidade", start)
        for neighbor in self.adj_list[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_road >= c_lib:
        return n * c_lib
    else:
        g = Graph()
        visited_cities = set()
        groups = []
    
        for city in range(1, n+1):
            g.add_city(city)
    
        for city in cities:
            g.add_edge(city[0],city[1])
            
        for city in range(1,n+1):
            if city not in visited_cities:
                current_group = set()
                g.dfs(city, current_group)
                groups.append(current_group)
                visited_cities.update(current_group)
        total_cost = 0
        for group in groups:
            num_cities = len(group)
            lib_cost = num_cities * c_lib
            road_cost = c_lib + (num_cities - 1) * c_road
            total_cost += min(lib_cost, road_cost)
        
        return total_cost

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
