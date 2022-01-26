# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int,input().split())

a = defaultdict(list)
for i in range(1, n + 1):
    a[input()].append(i)


for i in range(1, m + 1):
    key = input()
    if len(a[key]) > 0:
        print(" ".join(str(c) for c in a[key]))
    else:
        print(-1)
