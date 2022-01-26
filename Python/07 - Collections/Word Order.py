"""
Author: Eda AYDIN
"""
from collections import Counter

n = int(input())
word_list = []

for i in range(n):
    word_list.append(input().strip())

count = Counter(word_list)

print(len(count))
print(*count.values())
