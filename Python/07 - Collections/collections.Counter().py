"""
Author: Eda AYDIN

X: number of shoes
List of all the shoe sizes in the shop
N : number of customers
"""
from collections import Counter

X = int(input())
stock = Counter(map(int, input().split()))
N = int(input())

total_revenue = 0

for i in range(N):
    size, price = map(int, input().split())
    if stock[size]:
        total_revenue += price
        stock[size] -= 1

print(total_revenue)
