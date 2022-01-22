# Enter your code here. Read input from STDIN. Print output to STDOUT
integers = list(map(int, input().split()))
n = integers[0]
m = integers[1]

element_n = input().split()
elements_A = set(input().split())
elements_B = set(input().split())

counter = 0

for i in element_n:
    if i in elements_A:
        counter += 1
    if i in elements_B:
        counter -=1

print(counter)