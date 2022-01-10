# 1018 - 체스판 다시 칠하기

n, m = map(int, input().split())

board = list()
for _ in range(n):
    board.append(input())

black_start = 1
white_start = 1

min_change = 9999

for i in range(n-7):
    for j in range(m-7):
        b_count = 0
        w_count = 0
        for row in range(i, i+8):
            check = list(board[row])
            for col in range(j, j+8):

                # 정사각형의 (0, 0)이 B일 때
                if check[col] == 'W' and black_start == 1:
                    b_count += 1

                if check[col] == 'B' and black_start == -1:
                    b_count += 1

                # 정사각형의 (0, 0)이 W일 때
                if check[col] == 'B' and white_start == 1:
                    w_count += 1

                if check[col] == 'W' and white_start == -1:
                    w_count += 1

                black_start *= -1
                white_start *= -1

            black_start *= -1
            white_start *= -1

        if b_count < min_change:
            min_change = b_count

        if w_count < min_change:
            min_change = w_count

print(min_change)
