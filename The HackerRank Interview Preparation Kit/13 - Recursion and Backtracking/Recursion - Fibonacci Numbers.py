def fibonacci(number):
    # Write your code here.
    if number == 0:
        return 0
    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))
