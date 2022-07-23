
# 2606 - 바이러스

# 컴퓨터의 수
n = int(input())

# 네트워크 연결 쌍
m = int(input())

graph = {}

for _ in range(m):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u]=[v]
    else:
        graph[u].append(v)

    if v not in graph:
        graph[v] = [u]
    else:
        graph[v].append(u)


def dfs(root):
    visited = []
    stack = [root]

    while stack:
        computer = stack.pop()
        if computer not in visited:
            visited.append(computer)

            stack.extend(graph[computer])

    print(len(visited)-1)


dfs(1)
