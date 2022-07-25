# 7569 - 토마토 2

import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

tomato_map = [[] for depth in range(h)]
for z in range(h):
    for _ in range(n):
        tomato_map[z].append(list(map(int, sys.stdin.readline().split())))

# print(tomato_map)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
dz = [-1, 1]

queue = deque()


def bfs():
    while queue:
        z, x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and tomato_map[z][nx][ny] == 0:
                tomato_map[z][nx][ny] = tomato_map[z][x][y] + 1
                queue.append((z, nx, ny))

        for k in range(2):
            nz = z + dz[k]
            if 0 <= nz < h and tomato_map[nz][x][y] == 0:
                tomato_map[nz][x][y] = tomato_map[z][x][y] + 1
                queue.append((nz, x, y))


z = 0
i = -1
while i < n:
    i += 1
    for j in range(m):
        if tomato_map[z][i][j] == 1:
            queue.append((z, i, j))
    if i == n - 1:
        z += 1
        i = -1
        if z == h:
            break

flag = True
for tomato in tomato_map:
    for t in tomato:
        if 0 in t:
            flag = False

if flag:
    print(0)
    exit(0)


bfs()

# for tomato in tomato_map:
#     for t in tomato:
#         print(*t, sep=' ')

max_day = 0

for tomato in tomato_map:
    for t in tomato:
        if 0 in t:
            max_day = 0
            break
        max_day = max(max_day, max(t))

print(max_day - 1)
