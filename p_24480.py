# 24479 - 알고리즘 수업 - 깊이 우선 탐색 2

N, M, R = map(int, input().split())

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
    graph[K].sort(reverse=True)


def dfs(root):
    cnt = 1
    visited = {}
    stack = [root]

    while stack:
        pop = stack.pop()
        if pop not in visited:
            visited[pop] = cnt
            cnt += 1

            if pop in graph:
                stack.extend(reversed(graph[pop]))

    for i in range(1, N+1):
        if i in visited:
            print(visited[i])
        else:
            print(0)


dfs(R)
