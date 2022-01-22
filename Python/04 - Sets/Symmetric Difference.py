m = int(input())
m_integers = set(map(int, input().split()))
n = int(input())
n_integers = set(map(int, input().split()))

m_n = m_integers.difference(n_integers)
n_m = n_integers.difference(m_integers)

union = m_n.union(n_m)

result = list(union)
result.sort()

for i in range(len(result)):
    print(result[i])
