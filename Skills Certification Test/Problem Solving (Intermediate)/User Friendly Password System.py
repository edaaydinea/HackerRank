#!/bin/python3

import math
import os
import random
import re
import sys
import string


#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#


P = 131
M = 10**9 + 7
PP = [P**i for i in range(11)]
APPENDS = [""] + list(string.ascii_letters) + [str(d) for d in range(10)]

def calculate_hashing(pw):
    current_hash = 0
    for i in range(len(pw)):
        current_hash += ord(pw[-(i+1)]) * PP[i]
    return current_hash % M

def authEvents(events):
    current_hash = None
    good_hashs = None
    ans = []
    for event, value in events:
        if event == "setPassword":
            good_hashs = set(calculate_hashing(value + x) for x in APPENDS)
        else:
            assert event == "authorize"
            ans.append(1 if int(value) in good_hashs else 0)
    return ans
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    events_rows = int(input().strip())
    events_columns = int(input().strip())

    events = []

    for _ in range(events_rows):
        events.append(input().rstrip().split())

    result = authEvents(events)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
