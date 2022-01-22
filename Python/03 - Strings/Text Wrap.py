import textwrap

def wrap(string, max_width):
    string = [i for i in string]

    for i in range(max_width, len(string) + max_width, max_width+1):
        string.insert(i,"\n")
    return ("").join(string)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)