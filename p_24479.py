# 24479 - 알고리즘 수업 - 깊이 우선 탐색 1

import numpy as np

N, M, R = map(int, input().split())

row, col = N + 1, N + 1
graph = np.zeros((row, col), dtype=int)

for x in range(M):
    r, c = map(int, input().split())
    graph[r][c] = 1
    graph[c][r] = 1

# print(graph)

visited = [0] * (N + 1)


def dfs(f):
    visited[f] = 1
    print(f)

    flag = 0
    for n in range(1, N+1):
        if graph[f][n] == 1:
            if visited[n] == 0:
                dfs(n)
                flag = 1
    if flag == 0:
        print(0)
        return 0


dfs(R)
