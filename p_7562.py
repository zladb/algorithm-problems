# 7562 - 나이트의 이동

from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]


def bfs(start):
    visited = {start: 0}
    queue = deque([start])

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            print(visited[(x, y)])
            break

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and (nx, ny) not in visited:
                visited[(nx, ny)] = visited[(x, y)] + 1
                queue.append((nx, ny))


T = int(input())
for _ in range(T):
    I = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    bfs(start)
