# 1012 - 유기농 배추

from pprint import pprint

# 테스트 케이스 개수
T = int(input())


def check(x, y):
    if 0 <= x <= N - 1 and 0 <= y <= M - 1:
        if field[x][y] == 1:
            field[x][y] = 0

            # if x+1 <= N-1 and field[x+1][y] == 1:
            #     check(x + 1, y)  # right
            #
            # if y+1 <= M-1 and field[x][y+1] == 1:
            #     check(x, y + 1)  # right
            #
            # if x-1 >= 0 and field[x-1][y] == 1:
            #     check(x - 1, y)  # right
            #
            # if y-1 >= 0 and field[x][y-1] == 1:
            #     check(x, y-1)  # right

            check(x + 1, y)  # right
            check(x - 1, y)  # left
            check(x, y - 1)  # up
            check(x, y + 1)  # down
    else:
        return 0


for _ in range(T):
    # M - 가로길이 (1<=M<=50), N - 세로길이 (1<=N<=50), K - 배추가 심어져 있는 위치의 개수 (1<=K<=2500)
    M, N, K = map(int, input().split())

    field = [[0 for j in range(M)] for i in range(N)]

    for _ in range(K):
        row, col = map(int, input().split())
        field[col][row] = 1

    cnt = 0

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                cnt += 1
                check(i, j)

    print(cnt)
