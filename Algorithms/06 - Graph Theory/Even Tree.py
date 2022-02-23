#!/usr/bin/python3
from collections import deque

tree_length, edges = map(int, input().strip().split())
tree = [list() for i in range(tree_length)]

for i in range(edges):
    parent, child = map(int, input().strip().split())
    parent -= 1
    child -= 1
    tree[parent].append(child)
    tree[child].append(parent)


def reconstruct(tree):
    visited = [False] * len(tree)
    queue = deque([0])
    reconstructed = [list() for i in range(len(tree))]
    while len(queue) > 0:
        current = queue.popleft()
        visited[current] = True
        for i in tree[current]:
            if not visited[i]:
                reconstructed[current].append(i)
                queue.append(i)
    return reconstructed


cuts = 0


def dfs(tree, index):
    global cuts
    subtrees = []
    for i in tree[index]:
        subtrees.append(dfs(tree, i))
    for vertices in subtrees[:]:
        if not vertices % 2:
            cuts += 1
            subtrees.remove(vertices)

    return sum(subtrees) + 1


tree = reconstruct(tree)
dfs(tree, 0)
print(cuts)
