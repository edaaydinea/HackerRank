"""
In this challenge, the task is to debug the existing code to successfully execute all provided test files.

Given two strings consisting of digits 0 and 1 only, find the XOR of the two strings.

To calculate the XOR of two binary strings, find the sum of the two strings, and if a position contains two 1s, convert that position to 0. Return the resulting string.

Note: You can modify at most three lines in the given code and you cannot add or remove lines to the code. To restore the original code in the editor.

Sample Input:
10101
00101

Explanation:
1 + 0 = 1
0 + 0 = 0
1 + 1 = 0
0 + 0 = 0
1 + 1 = 0

Add the results to get 10000, which is the answer.

Sample Output:
10000
"""

def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'

    return res

s = input()
t = input()
print(strings_xor(s, t))



