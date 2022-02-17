from operator import attrgetter


def lcp(s, t):
    length = min(len(s), len(t))
    for i in range(length):
        if s[i] != t[i]:
            return i
    return length


class Suffix(object):
    def __init__(self, s):
        self.t = s
        self.start = 0
        self.c = -1

    def count(self, s):
        if s:
            self.start = lcp(self.t, s.t)
        self.c = len(self.t) - self.start


class SuffixArray(object):
    def __init__(self):
        self.suffixes = []

    def add(self, s):
        for i in range(len(s)):
            self.suffixes.append(Suffix(s[i:]))

    def select(self, i):
        for j in range(len(self.suffixes)):
            suffix = self.suffixes[j]
            if suffix.c == -1:
                if j == 0:
                    suffix.count(None)
                else:
                    suffix.count(self.suffixes[j - 1])
            if i <= suffix.c:
                return suffix.t[:suffix.start + i]
            else:
                i = i - suffix.c
        return 'INVALID'


def makeSuffixArray():
    sa = SuffixArray()
    n = int(input())
    for i in range(n):
        w = input()
        sa.add(w)
    sa.suffixes.sort(key=attrgetter('t'))
    return sa


def selectOutput():
    sa = makeSuffixArray()
    q = int(input())
    for i in range(q):
        k = int(input())
        print(sa.select(k))


if __name__ == "__main__":
    selectOutput()
