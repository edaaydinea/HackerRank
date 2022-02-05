#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minTime function below.
def minTime(machines, goal):
    machines, count = sorted(machines), len(machines)
    min_day = math.ceil(goal / count) * machines[0]
    max_day = math.ceil(goal / count) * machines[-1]

    while min_day < max_day:
        day = (max_day + min_day) // 2
        day_sum = sum(day // m for m in machines)

        if day_sum >= goal:
            max_day = day
        else:
            min_day = day + 1

    return min_day


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
