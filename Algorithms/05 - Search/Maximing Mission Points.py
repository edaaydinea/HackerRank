#!/bin/python3
import bisect
import collections

Place = collections.namedtuple("Place", "lat, long, height, points")

chunkplaces = {}
chunkvals = {}

giant = False


def getKey(place, off_lat=0, off_long=0):
    return ((place.lat // d_lat + off_lat) * 200011) + place.long // d_long + off_long


def getBestInChunk(place, key, best):
    if key not in chunkvals:
        return 0
    for i, (cand, val) in enumerate(zip(chunkplaces[key], chunkvals[key])):
        if -val < best:
            return 0
        if abs(place.lat - cand.lat) <= d_lat and abs(place.long - cand.long) <= d_long:
            return -val

    return 0


def getBest(place):
    best = 0
    for i in [0, 1, -1]:
        for j in [0, 1, -1]:
            key = getKey(place, i, j)
            ret = getBestInChunk(place, key, best)
            if ret > best:
                best = ret
    return best


def recordValue(place, val):
    if val < 0:
        return
    key = getKey(place)
    if key not in chunkplaces:
        chunkplaces[key] = []
        chunkvals[key] = []
    if giant:
        if len(chunkplaces[key]) == 0:
            chunkvals[key].append(-val)
            chunkplaces[key].append(place)
        else:
            if val < -chunkvals[key][0]:
                return
            else:
                chunkvals[key][0] = -val
                chunkplaces[key][0] = place
    else:
        i = bisect.bisect_left(chunkvals[key], -val)
        chunkplaces[key].insert(i, place)
        chunkvals[key].insert(i, -val)


def calculateValue(place):
    val = place.points + getBest(place)
    recordValue(place, val)
    return val


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d_lat = int(first_multiple_input[1])

    d_long = int(first_multiple_input[2])

    places = []

    if d_lat == 200000:
        giant = True

    for n_itr in range(n):
        second_multiple_input = input().rstrip().split()

        latitude = int(second_multiple_input[0])

        longitude = int(second_multiple_input[1])

        height = int(second_multiple_input[2])

        points = int(second_multiple_input[3])

        # Write your code here
        places.append(Place(latitude, longitude, height, points))

    places.sort(key=lambda p: -p.height)
    best = 0
    for p in places:
        ret = calculateValue(p)
        if ret > best:
            best = ret

    print(best)
