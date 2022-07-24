# 10026 - 적록색약

from pprint import pprint
import copy
from collections import deque

n = int(input())

color_map = []
for _ in range(n):
    color_map.append(list(' '.join(input()).split()))

new_color_map = copy.deepcopy(color_map)


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(cmap, root, color):
    visited = []
    queue = deque([root])

    while queue:
        x, y = queue.popleft()
        if cmap[x][y] == color:
            cmap[x][y] = 'x'
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    queue.append((nx, ny))


cnt1 = 0
cnt2 = 0

for i in range(n):
    for j in range(n):
        if color_map[i][j] != 'x':
            bfs(color_map, (i, j), color_map[i][j])
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if new_color_map[i][j] == 'R':
            new_color_map[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if new_color_map[i][j] != 'x':
            bfs(new_color_map, (i, j), new_color_map[i][j])
            cnt2 += 1

print(cnt1, cnt2)
