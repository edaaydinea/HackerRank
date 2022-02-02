#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
        a = list(sorted(set(a)))
        b = list(sorted(set(b)))
        c = list(sorted(set(c)))

        p = 0
        q = 0
        r = 0

        answer = 0

        while q < len(b):
            while p < len(a) and a[p] <= b[q]:
                p += 1
            while r < len(c) and c[r] <= b[q]:
                r += 1

            answer += p * r
            q += 1

        return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
