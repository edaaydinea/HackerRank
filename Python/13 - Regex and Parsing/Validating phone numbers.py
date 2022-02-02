import re

N = int(input())

for i in range(N):
    number = input()
    if 2 <= len(number) <= 15 and number.isdigit():
        output = re.findall(r"^[789]\d{9}$", number)
        if len(output) == 1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
