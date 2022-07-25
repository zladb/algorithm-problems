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

queue = deque()


def bfs():
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and tomato_map[nx][ny] == 0:
                tomato_map[nx][ny] = tomato_map[x][y] + 1
                queue.append((nx, ny))


for i in range(n):
    for j in range(m):
        if tomato_map[i][j] == 1:
            queue.append((i, j))

bfs()

# for tomato in tomato_map:
#     print(*tomato, sep=' ')

max_day = 0

for tomato in tomato_map:
    if 0 in tomato:
        max_day = 0
        break
    max_day = max(max_day, max(tomato))

print(max_day - 1)
