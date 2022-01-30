cube = lambda x: x**3 # complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    storage = [0,1]
    for i in range(2,n):
        storage.append(storage[i -1] + storage[i - 2])
    return storage[0:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))