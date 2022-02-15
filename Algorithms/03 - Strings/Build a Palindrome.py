#!/bin/python3

import os


#
# Complete the 'buildPalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
def build_palindrome_lookup(s):
    sx = '|' + '|'.join(s) + '|'
    sxlen = len(sx)
    rslt = [0] * sxlen
    c, r, m, n = 0, 0, 0, 0
    for i in range(1, sxlen):
        if i > r:
            rslt[i] = 0
            m = i - 1
            n = i + 1
        else:
            i2 = c * 2 - i
            if rslt[i2] < r - i:
                rslt[i] = rslt[i2]
                m = -1
            else:
                rslt[i] = r - i
                n = r + 1
                m = i * 2 - n
        while m >= 0 and n < sxlen and sx[m] == sx[n]:
            rslt[i] += 1
            m -= 1
            n += 1
        if i + rslt[i] > r:
            r = i + rslt[i]
            c = i
    res = [0] * len(s)
    for i in range(1, sxlen - 1):
        idx = (i - rslt[i]) // 2
        res[idx] = max(res[idx], rslt[i])
    return res


class state:
    def __init__(self):
        self.link = -1
        self.length = 0
        self.childs = {}


def build_part_st(a, st, num, last, sz):
    for c in a:
        cur = sz
        sz += 1
        st[cur].length = st[last].length + 1
        p = last
        while p != -1 and c not in st[p].childs:
            st[p].childs[c] = cur
            p = st[p].link
        if p == -1:
            st[cur].link = 0
        else:
            q = st[p].childs[c]
            if st[p].length + 1 == st[q].length:
                st[cur].link = q
            else:
                clone = sz
                sz += 1
                st[clone].length = st[p].length + 1
                st[clone].childs = dict((x, y) for (x, y) in st[q].childs.items())
                st[clone].link = st[q].link
                while p != -1 and st[p].childs[c] == q:
                    st[p].childs[c] = clone
                    p = st[p].link
                st[q].link = clone
                st[cur].link = clone
        last = cur
    return last, sz


def print_st(st):
    i = 0
    for s in st:
        print('#{} link:{} childs:{}'.format(i, s.link, s.childs))
        i += 1


def solve(a, b):
    n = len(a)
    blen = len(b)
    st = [state() for x in range(2 * n)]
    st[0].link = -1
    st[0].length = 0
    last = 0
    sz = 1
    last, sz = build_part_st(a, st, 1, last, sz)
    plookup = build_palindrome_lookup(b)
    apos, start, left, mid, total, curlen = 0, -1, 0, 0, 0, 0
    for i in range(blen):
        c = b[i]
        if c not in st[apos].childs:
            while apos != -1 and c not in st[apos].childs:
                apos = st[apos].link
            if apos == -1:
                apos = 0
                curlen = 0
                continue
            curlen = st[apos].length
        curlen += 1
        apos = st[apos].childs[c]
        new_start = i - curlen + 1
        new_mid = 0
        if i + 1 < blen:
            new_mid = plookup[i + 1]
        new_total = 2 * curlen + new_mid
        if total < new_total or (total == new_total and lex_gt(b, start, new_start, curlen + mid)):
            left = curlen
            mid = new_mid
            total = new_total
            start = new_start
    palindrome = []
    for i in range(left + mid):
        palindrome.append(b[start + i])
    for i in range(left - 1, -1, -1):
        palindrome.append(palindrome[i])
    return ''.join(palindrome)


def lex_gt(s, old_start, new_start, size):
    for i in range(size):
        if s[old_start + i] != s[new_start + i]:
            if s[old_start + i] > s[new_start + i]:  # old lex greater so pick new one
                return True
            break
    return False


def suffic_automate(a, b):
    rb = b[::-1]  # reverse b
    result1 = solve(a, rb)
    result2 = solve(rb, a)
    final_result = None
    if len(result1) > len(result2):
        final_result = result1
    elif len(result1) < len(result2):
        final_result = result2
    else:
        final_result = result1 if result1 < result2 else result2
    if len(final_result) == 0:
        return '-1'
    return final_result


def process_helper(a, b):
    return suffic_automate(a, b)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a = input()

        b = input()

        result = process_helper(a, b)

        fptr.write(result + '\n')

    fptr.close()
