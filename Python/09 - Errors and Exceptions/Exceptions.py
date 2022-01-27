for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError as z:
        print(f"Error Code: {z}")
    except ValueError as v:
        print(f"Error Code: {v}")
