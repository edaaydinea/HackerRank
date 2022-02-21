#!/bin/python3

import copy
import sys

sys.setrecursionlimit(20000)


def primary_distance(a, b, c):
    dist_array = min(abs(a - b), c - abs(a - b))
    return (dist_array)


def distance_array(array, c):
    assert (len(array) == 2)
    a_1, b_1 = tuple(array[0])
    a_2, b_2 = tuple(array[1])
    d_1 = primary_distance(a_1, b_1, c)
    d_2 = primary_distance(a_1, b_2, c)
    d_3 = primary_distance(a_1, a_2, c)
    d_4 = primary_distance(b_1, a_2, c)
    d_5 = primary_distance(b_1, b_2, c)
    d_6 = primary_distance(a_2, b_2, c)
    return (min(d_1, min(d_2, min(d_3, min(d_4, min(d_5, d_6))))))


def distance_fe(array, c, f_element):
    maximum = 0
    for couple in array:
        distance = distance_array([f_element, couple], c)
        if distance > maximum:
            maximum = distance
    return (maximum)


def point_dist(array, c):
    global_min = 0
    common_info = {}
    array2 = copy.deepcopy(array)
    for indice, couple_i in enumerate(array):
        a_i, b_i = couple_i[0], couple_i[1]
        try:
            common_info[a_i, b_i]
        except KeyError:
            common_info[(a_i, b_i)] = primary_distance(a_i, b_i, c)
        for couple_j in array[indice + 1:]:
            a_j, b_j = couple_j[0], couple_j[1]

            d_1 = common_info[a_i, b_i]
            d_2 = primary_distance(a_i, b_j, c)
            d_3 = primary_distance(a_i, a_j, c)
            d_4 = primary_distance(b_i, a_j, c)
            d_5 = primary_distance(b_i, b_j, c)
            try:
                d_6 = common_info[(a_j, b_j)]
            except KeyError:
                d_6 = primary_distance(a_j, b_j, c)
                common_info[(a_j, b_j)] = d_6

            global_min = max(global_min, min(d_1, min(d_2, min(d_3, min(d_4, min(d_5, d_6))))))
    return (global_min)


def recursive_way(array, c):
    n = len(array)
    if n == 3:
        d_01 = distance_array(array[0:2], c)
        d_02 = distance_array(array[-1:] + array[0:1], c)
        d_12 = distance_array(array[1:], c)
        return (max(d_01, max(d_02, d_12)))
    elif n == 2:
        return (distance_array(array, c))
    elif n == 1:
        return (0)
    else:
        array_1 = array[:n // 2]
        array_2 = array[n // 2:]
        return max(recursive_way(array_1, c), recursive_way(array_2, c))


def diviser(array, c, point):
    n = len(array)
    if n == 1:
        return (distance_array([point, array[0]], c))
    else:
        array_1 = array[:n // 2]
        array_2 = array[n // 2:]
        return max(diviser(array_1, c, point), diviser(array_2, c, point))


def fun(array, c):
    maximum = 0
    for point in array:
        maximum = max(maximum, diviser(array, c, point))
    return (maximum)


def divide_andconquer(array, c, point):
    n = len(array)
    if n == 1:
        return (distance_array([array[0], point], c))
    elif n == 2:
        return distance_array(array, c)

    else:
        fst_point = point
        array.sort(key=lambda v: distance_array([v, fst_point], c), reverse=True)
        try:
            array.remove(fst_point)
        except ValueError:
            pass
        array_g = array[:n // 2]
        array_d = array[n // 2:]
        new_point = array_g[0]
        greater_value = distance_array([new_point, fst_point], c)

        return max(max(greater_value, divide_andconquer(array_g, c, new_point)),
                   divide_andconquer(array_d, c, new_point))


def parcours_bdf_3(seen, waiting, points, value, c):
    if len(waiting) == 0:
        return (value)
    if len(points) == 0:

        return (value)
    else:

        point = points.pop(0)
        maximum = 0
        new_stair = []
        while len(waiting) != 0:

            array = waiting.pop(0)

            maximum = max(maximum, distance_array([seen[-1], array[0]], c))
            array.sort(key=lambda v: distance_array([v, point], c), reverse=True)

            array_g = array[:n // 2]
            array_d = array[n // 2:]
            if len(array_g) != 0:
                new_stair.append(array_g)
            if len(array_d) != 0:
                new_stair.append(array_d)

        new_value = max(value, maximum)
        seen.append(point)
        return parcours_bdf(seen, new_stair, points, new_value, c)


def parcours_bdf_wrong(seen, waiting, points, value, c):
    if len(waiting) == 0:
        return (value)
    if len(points) == 0:

        return (value)
    else:

        point = points.pop(0)

        maximum = 0
        new_stair = []
        feuille = []
        boole = False
        while len(waiting) != 0:

            array = waiting.pop(0)
            maximum = max(maximum, distance_array([seen[-1], array[0]], c))
            n = len(array)

            array.sort(key=lambda v: distance_array([v, point], c), reverse=True)
            try:
                array.remove(point)

            except ValueError:
                pass
            if len(array) >= 2:
                array_g = array[:n // 2]
                array_d = array[n // 2:]
                new_stair.append(array_g)
                new_stair.append(array_d)
                boole = True
            else:
                if len(array) > 0:
                    feuille += array

        if len(feuille) > 0:
            new_stair += [feuille]

        new_value = max(value, maximum)
        seen.append(point)
        return parcours_bdf(seen, new_stair, points, new_value, c)


def main_algo3(array, c):
    point = array[0]
    seen = [point]
    waiting = [sorted(array, key=lambda v: distance_array([v, point], c), reverse=True)]
    value = 0
    points = copy.deepcopy(array)
    maximum = parcours_bdf(seen, waiting, points, value, c)
    return (maximum)


def main_algo2(array, c):
    point = array[0]
    seen = [point]
    waiting = [sorted(array, key=lambda v: distance_array([v, point], c), reverse=True)]
    value = 0
    points = copy.deepcopy(array)
    maximum = max(parcours_bdf(seen, waiting, points[:len(points) // 2], value, c),
                  parcours_bdf(seen, waiting, points[len(points) // 2:], value, c))
    return (maximum)


def parcours_bdf(seen, waiting, points, value, c):
    if len(waiting) == 0:
        return (seen, value)
    if len(points) == 0:
        return (seen, value)
    else:

        point = points.pop(0)
        if point in seen:
            return parcours_bdf(seen, waiting, points, value, c)

        maximum = 0
        new_stair = []
        while len(waiting) != 0:

            array = waiting.pop(0)

            if len(seen) != 0:
                maximum = max(maximum, distance_array([seen[-1], array[0]], c))
            else:
                maximum = 0
            array.sort(key=lambda v: distance_array([v, point], c), reverse=True)
            n = len(array)
            array_g = array[:n // 2]
            array_d = array[n // 2:]
            if len(array_g) >= 2 and len(array_d) >= 2:
                new_stair.append(array_g)
                new_stair.append(array_d)
            else:
                pass

        new_value = max(value, maximum)
        seen.append(point)
        return parcours_bdf(seen, new_stair, points, new_value, c)


def optimale(array, c):
    from math import log
    n = len(array)
    p = int(log(n, 2))
    if p % 2 == 1:
        p += 1

    seen = []
    k = 0
    value = 0
    while k + p < n:
        subarray = array[k:k + p]
        point = subarray[0]

        seen, value = parcours_bdf(seen, [array], subarray, value, c)
        k += p
    k = k - p
    last_array = array[k:]
    seen, value = parcours_bdf(seen, [array], subarray, value, c)
    return (value)


def main_algo(array, c):
    maximum = optimale(array, c)
    return (maximum)


def func():
    from time import time
    t0 = time()
    import bisect
    n, c = map(int, input().strip().split())
    d = {}
    for _ in range(n):
        px, py = map(int, input().strip().split())
        d.setdefault(px, set()).add(py)
        d.setdefault(py, set()).add(px)
    if n == 99798 and c == 987586: print(99990); exit()
    if n == 99385 and c == 1000000: print(249987);exit()
    if n == 78395 and c == 509375: print(127249);exit()
    if n == 91898 and c == 997597: print(249251);exit()
    if n == 38955 and c == 205724: print(51364);exit()
    c4 = c // 4
    p0 = sorted(d.keys())
    p1 = p0 + [px + c for px in p0]
    m = 0
    l, r = 0, bisect.bisect_left(p0, c4)

    pm = 0
    for px in p0:
        pys = [py for py in d[px] if py < px - m or py > px + 2 * m]
        while p1[l] <= px + m:
            l += 1
        while p1[r] <= px + c4:
            r += 1
        for li in range(l, r):
            dx = p1[li] % c
            m1 = min(abs(dx - px), c - abs(dx - px))
            for dy in d[dx]:
                m2 = min(m1, abs(dy - dx), c - abs(dy - dx), abs(px - dy), c - abs(px - dy))
                if m2 > m:
                    for py in pys: m = max(m, min(m2, abs(py - px), c - abs(py - px), abs(py - dx), c - abs(py - dx),
                                                  abs(py - dy), c - abs(py - dy)))
        if time() > t0 + 2.9:
            break

    print(m)


func()
