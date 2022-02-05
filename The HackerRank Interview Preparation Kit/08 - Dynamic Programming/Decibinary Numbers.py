#!/bin/python3

import math
import os


def makeTable(dmax):
    bits = math.ceil(math.log2(dmax))
    table = [[0]*dmax for _ in range(bits)]
    for ii in range(10):
        table[0][ii] = 1
    for bit in range(1, bits):
        m2 = 1 << bit
        t0 = table[bit]
        t1 = table[bit-1]
        maxlen = 10**(bit+1)
        if maxlen > dmax:
            maxlen = dmax
        for ii in range(maxlen):
            pmax = ii//m2
            if pmax > 9:
                pmax = 9
            total = 0
            for pos in range(ii - pmax*m2, ii + m2, m2):
                total += t1[pos]
            t0[ii] = total
    return table


lookup = makeTable(287000)
agg = lookup[-1][:]
for ii in range(1, len(agg)):
    agg[ii] += agg[ii-1]


def decibinaryHelper(num, x):
    pos = 0
    result = 0
    for bit in range(len(lookup)-1, 0, -1):
        digit = 1 << bit
        tl = lookup[bit-1]
        for kk in range(0, (num//digit) + 1):
            remain = num - kk*digit
            count = tl[remain]
            if (pos + count) <= x:
                pos += count
            else:
                result = (result * 10) + kk
                num = remain
                break
    result = (result * 10) + num
    return result


def findNum(x):
    start = 1
    end = len(agg) - 1
    while start != end:
        num = (start + end) // 2
        if agg[num] == x:
            return num
        elif agg[num] > x:
            end = num
        else:
            start = num + 1
    return start


# Complete the decibinaryNumbers function below.
def decibinaryNumbers(x):
    if x == 1:
        return 0
    num = findNum(x)
    pos = agg[num-1] + 1
    result = decibinaryHelper(num, x-pos)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        x = int(input())

        result = decibinaryNumbers(x)

        fptr.write(str(result) + '\n')

    fptr.close()