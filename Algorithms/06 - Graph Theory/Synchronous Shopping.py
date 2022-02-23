#!/bin/python3

import heapq
import os


#
# Complete the 'shop' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. STRING_ARRAY centers
#  4. 2D_INTEGER_ARRAY roads
#


def shop(n, k, centers, roads):
    # Write your code here
    fish_masks = [0]
    all_fishes_mask = 2 ** k - 1
    f = 1
    for _ in range(k):
        fish_masks.append(f)
        f <<= 1

    cities = [0] * (n + 1)
    for idx, c_str in enumerate(centers):
        c_data = list(map(int, c_str.split()))
        if c_data[0] > 0:
            cities[idx + 1] = sum([fish_masks[i] for i in c_data[1:]])

    neighbours = [[] for _ in range(n + 1)]
    times = [[0] * (n + 1) for _ in range(n + 1)]
    for c1, c2, t in roads:
        neighbours[c1].append(c2)
        neighbours[c2].append(c1)
        times[c1][c2] = t
        times[c2][c1] = t

    q = [(1 << 10) + cities[1]]
    seen = [[False] * (all_fishes_mask + 1) for _ in range(n + 1)]
    trip_time = [[None] * (all_fishes_mask + 1) for _ in range(n + 1)]

    fish_mask = 2 ** 10 - 1
    node_mask = fish_mask << 10

    while q:
        data = heapq.heappop(q)
        time = data >> 20
        node = (data & node_mask) >> 10
        f_mask = data & fish_mask
        if seen[node][f_mask]:
            continue
        seen[node][f_mask] = True
        if (node == n) and (f_mask == all_fishes_mask):
            continue
        for nxt in neighbours[node]:
            nxt_mew_mask = cities[nxt] | f_mask
            if seen[nxt][nxt_mew_mask]:
                continue
            nxt_cur_time = trip_time[nxt][nxt_mew_mask]
            nxt_new_time = time + times[node][nxt]
            if (nxt_cur_time is not None) and (nxt_new_time >= nxt_cur_time):
                continue
            trip_time[nxt][nxt_mew_mask] = nxt_new_time
            heapq.heappush(q, (nxt_new_time << 20) + (nxt << 10) + nxt_mew_mask)

    rv = 0
    trip_times = trip_time[n]
    for mask_i, time_i in enumerate(trip_times):
        if not time_i:
            continue
        for data_j, time_j in enumerate(trip_times[mask_i:]):
            if not time_j:
                continue
            mask_j = mask_i + data_j
            mask = mask_i | mask_j
            t_time = max(time_i, time_j)
            if mask != all_fishes_mask:
                continue
            if rv and t_time >= rv:
                continue
            rv = t_time
    return rv


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    centers = []

    for _ in range(n):
        centers_item = input()
        centers.append(centers_item)

    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    res = shop(n, k, centers, roads)

    fptr.write(str(res) + '\n')

    fptr.close()
