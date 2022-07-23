# 24444 - 알고리즘 수업 - 너비 우선 탐색 1
import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())

graph = {}

for _ in range(M):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = [v]
    elif v not in graph[u]:
        graph[u].append(v)

    if v not in graph:
        graph[v] = [u]
    elif u not in graph[v]:
        graph[v].append(u)

for K in graph:
    graph[K].sort()

# print(graph)

def bfs(root):
    cnt = 1
    visited = {}
    queue = deque()
    queue.append(root)

    while queue:
        pop = queue.popleft()
        if pop not in visited:
            visited[pop] = cnt
            cnt += 1

            if pop in graph:
                queue.extend(graph[pop])
                # print(queue)

    # 출력
    for i in range(1, N+1):
        if i in visited:
            print(visited[i])
        else:
            print(0)


bfs(R)
