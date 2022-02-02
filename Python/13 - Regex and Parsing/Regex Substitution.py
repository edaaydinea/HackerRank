import re


def change(match):
    if match.group(1) == "&&":
        return "and"
    else:
        return "or"


for _ in range(int(input())):
    pattern = r"(?<= )(\|\||&&)(?= )"
    print(re.sub(pattern, change, input()))
