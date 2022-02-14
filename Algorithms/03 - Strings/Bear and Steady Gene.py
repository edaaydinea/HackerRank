#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#

def steadyGene(gene):
    # Write your code here
    min_length_string = len(gene)

    occurences = dict()
    occurences["A"] = 0
    occurences["C"] = 0
    occurences["G"] = 0
    occurences["T"] = 0

    expected = len(gene) // 4

    for g in gene:
        occurences[g] += 1

    for x in occurences:
        occurences[x] = max(0, occurences[x] - expected)

    if occurences['A'] == 0 and occurences['G'] == 0 and occurences['C'] == 0 and occurences['T'] == 0:
        return 0

    found = dict()
    found["A"] = 0
    found["C"] = 0
    found["G"] = 0
    found["T"] = 0

    tail = 0
    head = 0

    while head != len(gene):
        found[gene[head]] += 1
        if found["A"] >= occurences["A"] and \
                found["C"] >= occurences["C"] and \
                found["G"] >= occurences["G"] and \
                found["T"] >= occurences["T"]:
            min_length_string = min(min_length_string, head - tail + 1)

            while found[gene[tail]] > occurences[gene[tail]]:
                found[gene[tail]] -= 1
                tail += 1
                min_length_string = min(min_length_string, head - tail + 1)
        head += 1

    return min_length_string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
