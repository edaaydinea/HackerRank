#!/bin/python3
import itertools
import math
import os
import random
import re
import sys


#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic : list) -> list:
    # Write your code here
    maximum = 0
    teams = 0
    for p in itertools.combinations(topic, 2):
        combined_topics = bin(int(p[0],2) | int(p[1],2)).count("1")
        if combined_topics > maximum:
            maximum = combined_topics
            teams = 1
        elif combined_topics == maximum:
            teams += 1

    return [maximum, teams]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
