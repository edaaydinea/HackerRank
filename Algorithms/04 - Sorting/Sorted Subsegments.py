#!/bin/python3

import os


#
# Complete the 'sortedSubsegments' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#  3. 2D_INTEGER_ARRAY queries
#

def sortedSubsegments(n, q, k, a, queries):
    # Write your code here
    b = sorted(a)
    lmin, rmax, pmax, qmin = (n - 1), 0, 0, (n - 1)
    pmin, qmax, flag = (n - 1), 0, 1
    count, span_q, ladder, revlad = [], 0, 0, 0
    if q >= 2:
        ladder = all(queries[i + 1][0] > queries[i][0] for i in range(q - 1))
        revlad = all(queries[i + 1][1] < queries[i][1] for i in range(q - 1))

    if a != b and ladder < 1 and revlad < 1:
        for i in range(q):
            l, r = queries[i][0], queries[i][1]

            if (r - l) > (rmax - lmin):
                lmin, rmax = l, r

            if l < pmin:
                pmin, pmax = l, r
            elif l == pmin and pmax < r:
                pmax = r

            if r > qmax:
                qmin, qmax = l, r
            elif r == qmax and qmin > l:
                qmin = l

        for i in range(q):
            l, r = queries[i][0], queries[i][1]

            if l > lmin and r < rmax:
                continue
            if l > pmin and r < pmax:
                continue
            if l > qmin and r < qmax:
                continue

            if i < (q - 1):
                if l >= queries[i + 1][0] and r <= queries[i + 1][1]:
                    continue

            if i > 0:
                if l >= queries[i - flag][0] and r <= queries[i - flag][1]:
                    flag += 1
                    continue
                else:
                    flag = 1

            count += [i]
            span_q += r - l + 1

    # Perform Queries
    if ladder > 0:
        l, r, Qu = queries[0][0], queries[0][1], int((k + 5) / 5)
        a[l:r + 1] = sorted(a[l:r + 1])
        for i in range(1, q):
            l, r, r0, m, sig = queries[i][0], queries[i][1], queries[i - 1][1], 0, 0
            if l > r0 or (r - r0) > 0.1 * (r0 - l):
                a[l:r + 1] = sorted(a[l:r + 1])
                continue
            if k < l:
                break
            count = list(range(r0 + 1, r + 1))
            for j in range(len(count)):
                p, new_A = count[j], a[count[j]]
                l, r0 = queries[i][0], queries[i - 1][1]
                if a[l] >= new_A:
                    del (a[p])
                    a[l:l] = [new_A]
                    continue
                elif a[r0 + j - 1] <= new_A:
                    del (a[p])
                    a[r0 + j:r0 + j] = [new_A]
                    continue
                while sig < 1:
                    m = int((l + r0) / 2)
                    if a[m] > new_A:
                        r0 = m
                    elif a[m + 1] < new_A:
                        l = m + 1
                    else:
                        del (a[p])
                        a[m + 1:m + 1] = [new_A]
                        sig = 1

    elif revlad > 0:
        l, r, Qu = queries[0][0], queries[0][1], int((k + 5) / 5)
        a[l:r + 1] = sorted(a[l:r + 1])
        for i in range(1, q):
            l, r, l0, m, sig = queries[i][0], queries[i][1], queries[i - 1][0], 0, 0
            if k > r:
                break
            if r < l0:
                a[l:r + 1] = sorted(a[l:r + 1])
                continue
            count = list(range(l, l0))
            for j in range(len(count)):
                p, new_A = count[j], a[count[j]]
                if a[l0] >= new_A:
                    del (a[p])
                    a[l0:l0] = [new_A]
                    continue
                elif a[r] <= new_A:
                    del (a[p])
                    a[r:r] = [new_A]
                    continue
                while sig < 1:
                    m = int((l0 + r) / 2)
                    if a[m] > new_A:
                        r = m
                    elif a[m + 1] < new_A:
                        l0 = m + 1
                    else:
                        del (a[p])
                        a[m + 1:m + 1] = [new_A]
                        sig = 1

    elif span_q < 1e9 and a != b:
        for i in count:
            l, r = queries[i][0], queries[i][1]
            a[l:(r + 1)] = sorted(a[l:(r + 1)])
    else:
        a[pmin:qmax + 1] = sorted(a[pmin:qmax + 1])
    return a[k]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = sortedSubsegments(n, q, k, a, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
