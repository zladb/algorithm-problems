# 16928 - 뱀과 사다리 게임

from collections import deque
n, m = map(int, input().split())

ladder = {}
snake = {}

# 사다리 입력
for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

# 뱀 입력
for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v


def bfs():
    visited = {1: 0}
    queue = deque([1])

    while queue:
        # print(queue)
        # print(visited)
        spot = queue.popleft()

        if spot == 100:
            print(visited[spot])
            break

        for i in range(1, 7):
            nx = spot + i
            if 1 <= nx <= 100 and nx not in visited:

                if nx in ladder:
                    nx = ladder[nx]

                elif nx in snake:
                    nx = snake[nx]

                if nx not in visited:
                    visited[nx] = visited[spot] + 1
                    queue.append(nx)


bfs()
