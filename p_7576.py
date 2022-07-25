# 7576 - 토마토

from pprint import pprint
import copy

import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

tomato_map = []
for _ in range(n):
    tomato_map.append(list(map(int, sys.stdin.readline().split())))

# print(tomato_map)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(root):
    visited = []
    queue = deque([root])

    while queue:
        x, y, day = queue.popleft()
        if (x, y) not in visited:
            visited.append((x, y))
            if tomato_map[x][y] == 0 or tomato_map[x][y] >= day:
                tomato_map[x][y] = day
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if (nx, ny) not in visited:
                        if 0 <= nx < n and 0 <= ny < m and tomato_map[nx][ny] != -1:
                            queue.append((nx, ny, day+1))


for i in range(n):
    for j in range(m):
        if tomato_map[i][j] == 1:
            bfs((i, j, 1))

# for tomato in tomato_map:
#     print(*tomato, sep=' ')

# flag = False
# max_day = tomato_map[0][0]
# for i in range(n):
#     for j in range(m):
#         if tomato_map[i][j] == 0:
#             flag = True
#             max_day = 0
#             break
#         if tomato_map[i][j] > max_day:
#             max_day = tomato_map[i][j]
#     if flag:
#         break


max_day = 0

for tomato in tomato_map:
    if 0 in tomato:
        max_day = 0
        break
    if max_day < max(tomato):
        max_day = max(tomato)

print(max_day-1)

