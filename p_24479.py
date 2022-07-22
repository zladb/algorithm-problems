# 24479 - 알고리즘 수업 - 깊이 우선 탐색 1

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


def dfs(root):
    visited = []
    stack = [root]

    if root not in graph:
        print(0)
        return 0

    while stack:
        pop = stack.pop()
        if pop not in visited:
            visited.append(pop)
            print(pop)

            if pop in graph:
                temp = list(set(graph[pop]) - set(visited))
                temp.sort(reverse=True)
                stack.extend(temp)

    print(0)


dfs(R)
