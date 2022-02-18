#!/bin/python3

import os

#
# Complete the 'twoTwo' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING a as parameter.
#

tree = [False, {}]


def count(word):
    count = 0
    for start in range(len(word)):
        current, index = tree, start
        while True:
            if current[0]:
                count += 1
            try:
                current = current[1][word[index]]
                index += 1
            except (KeyError, IndexError):
                break
    return count


def add(word):
    current = tree
    for c in word:
        try:
            current = current[1][c]
        except KeyError:
            current[1][c] = [False, {}]
            current = current[1][c]
    current[0] = True


v = 1
for x in range(801):
    add(str(v)[::-1])
    v <<= 1


def twoTwo(a):
    # Write your code here
    done = {}
    if a not in done:
        done[a] = count(a[::-1])
    return done[a]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a = input()

        result = twoTwo(a)

        fptr.write(str(result) + '\n')

    fptr.close()
