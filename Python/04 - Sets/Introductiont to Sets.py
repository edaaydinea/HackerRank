def average(array):
    # your code goes here
    s = set(array)
    return float(sum(s) / len(s))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
