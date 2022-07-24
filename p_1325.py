# 1325 - 효율적인 해킹

import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

hacking = {}


def bfs(root):
    visited = [False for _ in range(n+1)]
    visited[root] = True
    queue = deque([root])
    cnt = 1

    while queue:
        node = queue.popleft()
        for nx in graph[node]:
            if not visited[nx]:
                visited[nx] = True
                queue.append(nx)
                cnt += 1

    return cnt


ans = []
maxi = 0
for i in range(1, n + 1):
    val = bfs(i)
    if val > maxi:
        maxi = val
        ans.clear()
        ans.append(i)
    elif val == maxi:
        ans.append(i)

print(*ans)
