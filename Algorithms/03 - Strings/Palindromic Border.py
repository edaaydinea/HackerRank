#!/bin/python3

import os


#
# Complete the 'palindromicBorder' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def monoString(s):
    cc = s[0]
    for c in s:
        if c != cc:
            return False
    return True


def monoStringResult(s):
    output = 0
    for i in range(2, len(s) + 1):
        output += i * (i - 1) // 2
        output %= 1000000007
    return output


def calculatePalindromeBorders(palindrome_dict):
    output = 0
    for palindrome, times in palindrome_dict.items():
        output += times * (times - 1) // 2
    return output


def palindromicBorder(s):
    # Write your code here
    if monoString(s):
        return monoStringResult(s)
    output = 0

    odd = [[], {}, 1]
    for c in s:
        if c not in odd[1]:
            odd[1][c] = 0
        odd[1][c] += 1
    for i in range(len(s)):
        odd[0].append(i)
    output += calculatePalindromeBorders(odd[1])

    even = [[], {}, 1]
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            even[0].append(i)
            ss = s[i:i + 2]
            if ss not in even[1]:
                even[1][ss] = 0
            even[1][ss] += 1
    output += calculatePalindromeBorders(even[1])

    for l in range(3, len(s)):
        if l % 2 == 0:
            working_tuple = even
        else:
            working_tuple = odd

        new_tuple = [[], {}, 1]
        for index in working_tuple[0]:
            if index - 1 >= 0 and index + l - 2 < len(s) and s[index - 1] == s[index + l - 2]:
                new_tuple[0].append(index - 1)
                ss = s[index - 1:index - 1 + l]
                if ss not in new_tuple[1]:
                    new_tuple[1][ss] = 0
                new_tuple[1][ss] += 1

        output += calculatePalindromeBorders(new_tuple[1])
        output %= 1000000007
        if l % 2 == 0:
            even = new_tuple
        else:
            odd = new_tuple
    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = palindromicBorder(s)

    fptr.write(str(result) + '\n')

    fptr.close()
