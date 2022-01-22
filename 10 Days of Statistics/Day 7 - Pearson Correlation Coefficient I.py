"""
Problem: https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem

Author: Eda AYDIN
"""
import statistics

n = int(float(input()))
dataset_X = list(map(float, input().split()))
dataset_Y = list(map(float, input().split()))


def pearson_correlation(n, dataset_x, dataset_y):
    mean_x = statistics.mean(dataset_x)
    mean_y = statistics.mean(dataset_y)
    std_x = statistics.pstdev(dataset_x)
    std_y = statistics.pstdev(dataset_y)
    summation = 0

    for i in range(n):
        summation += (dataset_x[i] - mean_x) * (dataset_y[i] - mean_y)

    return summation / (n * std_x * std_y)


print(round(pearson_correlation(n, dataset_X, dataset_Y), 3))
