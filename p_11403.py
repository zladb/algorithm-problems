# 11403 - 경로 찾기

from pprint import pprint

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

graph = {}

for i in range(n):
    for j in range(n):
        if matrix[i][j]:
            if i not in graph:
                graph[i] = [j]
            else:
                graph[i].append(j)

for i in range(0, n):
    if i in graph:
        graph[i].sort(reverse=True)
    else:
        graph[i] = []

answer = [[0 for _ in range(n)] for _ in range(n)]


def dfs(root):
    visited = []
    stack = [root]
    flag = 0

    while stack:
        node = stack.pop()
        if flag == 0:
            flag = 1
        else:
            answer[root][node] = 1
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])


for i in range(n):
    dfs(i)

for line in answer:
    print(*line, sep=' ')
