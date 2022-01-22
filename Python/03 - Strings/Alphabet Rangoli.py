import string

alpha = string.ascii_lowercase

def print_rangoli(size):
    # your code goes here
    lst = []
    for row in range(size):
        to_print = "-".join(alpha[row:size])
        lst.append(to_print[::-1] + to_print[1:])
    width = len(lst[0])

    for row in range(size - 1, 0 ,-1):
        print(lst[row].center(width, "-"))

    for row in range(size):
        print(lst[row].center(width, "-"))



