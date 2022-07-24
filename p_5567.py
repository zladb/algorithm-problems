# 5567 - 결혼식

n = int(input())
m = int(input())

graph = {}

for _ in range(m):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = [v]
    else:
        graph[u].append(v)

    if v not in graph:
        graph[v] = [u]
    else:
        graph[v].append(u)

for i in range(1, n + 1):
    if i in graph:
        graph[i].sort(reverse=True)
    else:
        graph[i] = []


def dfs(root):
    visited = []
    stack = [[root], [], [], []]

    for i in range(3):
        while stack[i]:
            node = stack[i].pop()
            if node not in visited:
                visited.append(node)
                stack[i+1].extend(graph[node])

    print(len(visited)-1)


dfs(1)
