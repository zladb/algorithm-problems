# 24444 - 알고리즘 수업 - 너비 우선 탐색 1
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

def bfs(root):
    cnt = 1
    visited = {}
    queue = deque([root])

    while queue:
        pop = queue.popleft()
        if pop not in visited:
            visited[pop] = cnt
            cnt += 1

            if pop in graph:
                queue += graph[pop]


    # 출력
    for i in range(1, N+1):
        if i in visited:
            print(visited[i])
        else:
            print(0)


bfs(R)
