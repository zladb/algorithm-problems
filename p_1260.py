# 1260 - DFS와 BFS

import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())

graph = {}

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph[u] = [v]
    else:
        graph[u].append(v)

    if v not in graph:
        graph[v] = [u]
    else:
        graph[v].append(u)

for K in graph:
    graph[K].sort()

# print(graph)

def dfs(root):
    cnt = 1
    visited = []
    stack = [root]

    while stack:
        pop = stack.pop()
        if pop not in visited:
            visited.append(pop)
            cnt += 1

            if pop in graph:
                stack.extend(reversed(graph[pop]))

    print(*visited, sep=' ')


def bfs(root):
    cnt = 1
    visited = []
    queue = deque([root])

    while queue:
        pop = queue.popleft()
        if pop not in visited:
            visited.append(pop)
            cnt += 1

            if pop in graph:
                queue += graph[pop]

    # 출력
    print(*visited, sep=' ')


dfs(R)
bfs(R)
