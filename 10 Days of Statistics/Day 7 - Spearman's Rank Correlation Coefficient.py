"""
Problem: https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem

Author: Eda AYDIN
"""


def rank(dataset):
    rank = {}
    sort = sorted(dataset)
    for i in range(len(dataset)):
        for j in range(len(sort)):
            if dataset[i] == sort[j]:
                rank[dataset[i]] = j + 1
    return rank


def spearman(dataset_x, dataset_y, rank_x, rank_y):
    difference_rank = 0
    for i in range(n):
        if rank_x[dataset_x[i]] != rank_y[dataset_y[i]]:
            difference_rank += (rank_x[dataset_x[i]] - rank_y[dataset_y[i]]) ** 2
    return (6 * difference_rank) / (n ** 3 - n)


n = int(float(input()))
dataset_X = list(map(float, input().split()))
dataset_Y = list(map(float, input().split()))

rank_X = rank(dataset_X)
rank_Y = rank(dataset_Y)

print(round(1 - spearman(dataset_X, dataset_Y, rank_X, rank_Y), 3))
