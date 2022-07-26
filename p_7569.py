# 7569 - 토마토 2

import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

tomato_map = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for depth in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()


def bfs():
    while queue:
        z, x, y = queue.popleft()

        for k in range(6):
            nz, nx, ny = z + dz[k], x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if tomato_map[nz][nx][ny] == 0:
                    tomato_map[nz][nx][ny] = tomato_map[z][x][y] + 1
                    queue.append((nz, nx, ny))


for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato_map[i][j][k] == 1:
                queue.append((i, j, k))

bfs()

# for tomato in tomato_map:
#     for t in tomato:
#         print(*t, sep=' ')

max_day = 0

ans = False

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato_map[i][j][k] == 0:
                ans = True

            max_day = max(max_day, tomato_map[i][j][k])

if ans:
    print(-1)
elif max_day == 1:
    print(0)
else:
    print(max_day - 1)
