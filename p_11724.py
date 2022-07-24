# 11724 - 연결 요소의 개수

n, m = map(int, input().split())

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

visited = []


def dfs(root):
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if len(graph[node]) > 0:
                stack.extend(graph[node])


cnt = 0

for i in range(1, n + 1):
    if i not in visited:
        cnt += 1
        dfs(i)

print(cnt)
