size_set = int(input())
set0 = set(map(int, input().split()))
iteration_number = int(input())

for i in range(iteration_number):
    set1 = input().split()
    if set1[0] == "pop":
        set0.pop()
    elif set1[0] == "remove":
        set0.remove(int(set1[1]))
    elif set1[0] == "discard":
        set0.discard(int(set1[1]))

print(sum(set0))