# p13460 - 구슬 탈출2
import sys
from collections import deque

N, M = map(int, input().split())

input = sys.stdin.readline

board = [list(input().strip()) for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

# for line in board:
#     print(''.join(line))
# print()

# 상 0, 우 1, 하 2, 좌 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j


def move(x, y, d):
    # 이동한 칸 수
    count = 0
    while board[x + dx[d]][y + dy[d]] != '#' and board[x][y] != 'O':
        x += dx[d]
        y += dy[d]
        count += 1
    return x, y, count


def bfs(rx, ry, bx, by):
    queue = deque([(rx, ry, bx, by, 1)])
    visited[rx][ry][bx][by] = True
    while queue:
        rx, ry, bx, by, depth = queue.popleft()

        if depth > 10:
            continue

        for d in range(4):
            moved_rx, moved_ry, red_count = move(rx, ry, d)
            moved_bx, moved_by, blue_count = move(bx, by, d)

            if board[moved_bx][moved_by] == 'O':
                continue
            if board[moved_rx][moved_ry] == 'O':
                print(1)
                return

            if (moved_rx, moved_ry) == (moved_bx, moved_by):
                if red_count > blue_count:
                    moved_rx -= dx[d]
                    moved_ry -= dy[d]
                if blue_count > red_count:
                    moved_bx -= dx[d]
                    moved_by -= dy[d]

            if visited[moved_rx][moved_ry][moved_bx][moved_by] == False:
                visited[moved_rx][moved_ry][moved_bx][moved_by] = True
                queue.append((moved_rx, moved_ry, moved_bx, moved_by, depth + 1))

    print(0)


bfs(rx, ry, bx, by)
