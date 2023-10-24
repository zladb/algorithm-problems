import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

if n == m == 1:
    print(1)
    exit()

road = [[c for c in input()] for _ in range(n)]

visited = [[k + 1 for _ in range(m)] for _ in range(n)]
visited[0][0] = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque([(0, 0, 0)])
res = 1

day_time = True
while q:
    q_length = len(q)
    for _ in range(q_length):
        r, c, w = q.popleft()

        if r == n - 1 and c == m - 1:
            print(res)
            exit()

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < n and 0 <= nc < m):
                # 맵의 범위를 벗어난다면
                continue

            if visited[nr][nc] <= w:
                # 이미 더 적은 방법으로 도달할 수 있다면
                continue

            # 낮
            if day_time:
                if road[nr][nc] == '0':  # 갈 수 있는 길이라면
                    visited[nr][nc] = w
                    q.append((nr, nc, w))
                else:
                    # 벽 부수는 횟수를 다 쓴 경우
                    if w == k:
                        continue

                    visited[nr][nc] = w
                    q.append((nr, nc, w + 1))
            else:
                if road[nr][nc] == '0':
                    visited[nr][nc] = w
                    q.append((nr, nc, w))
                else:
                    q.append((r, c, w))

    day_time = not day_time
    res += 1

print(-1)