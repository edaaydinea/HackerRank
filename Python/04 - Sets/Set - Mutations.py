# Enter your code here. Read input from STDIN. Print output to STDOUT
number_of_elements_in_A = int(input())
set_of_A = set(map(int, input().split()))

iteration = int(input())

for i in range(iteration):
    operation = input().split()
    new_set = set(map(int, input().split()))
    eval("set_of_A.{}({})".format(operation[0], new_set))

print(sum(set_of_A))