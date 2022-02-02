# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S, k = input(), input()
matches = re.finditer(r'(?=(' + k + '))', S)

anymatch = False

for match in matches:
    anymatch = True
    print((match.start(1), match.end(1) - 1))

if not anymatch:
    print((-1,-1))
