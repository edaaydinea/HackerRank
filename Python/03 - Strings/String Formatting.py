def print_formatted(number):
    # your code goes here
    for i in range(1, number +1):
        width = len(f"{number:b}")
        print(f"{i:{width}} {i:{width}o} {i:{width}X} {i:{width}b}")
