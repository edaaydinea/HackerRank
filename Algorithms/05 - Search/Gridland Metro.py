#!/bin/python3

import os


#
# Complete the 'gridlandMetro' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n : row number (matrix)
#  2. INTEGER m : column number (matrix)
#  3. INTEGER k : number of track
#  4. 2D_INTEGER_ARRAY track
#

def overLapped(c1, c2, g1, g2):
    if c1 == g2 + 1 or g1 == c2 + 1:
        return True
    elif g1 <= c1 <= g2 or g1 <= c2 <= g2:
        return True
    elif c1 <= g1 <= c2 or c1 <= g2 <= c2:
        return True


def updateGridland(gridland, r, c1, c2):
    if r not in gridland:
        gridland[r] = []
        gridland[r].append((c1, c2))
    else:
        trackadded = False
        for i in range(len(gridland[r])):
            if overLapped(c1, c2, gridland[r][i][0], gridland[r][i][1]):
                gridland[r][i] = (min(c1, gridland[r][i][0]), max(c2, gridland[r][i][1]))
                trackadded = True
                break
            if not trackadded:
                gridland[r].append((c1, c2))

    return gridland


def gridlandMetro(n, m, k, track):
    # Write your code here
    gridland = {}
    for t in track:
        r, c1, c2 = t
        updateGridland(gridland, r, c1, c2)

    used = 0
    for row in gridland:
        for track in gridland[row]:
            used += abs(track[0] - track[1]) + 1

    return n * m - used


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(tuple(map(int, input().rstrip().split())))
    tracks = tuple(track)

    result = gridlandMetro(n, m, k, tracks)

    fptr.write(str(result) + '\n')

    fptr.close()
