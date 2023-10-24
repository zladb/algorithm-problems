# 12100 - 2048 (easy)
import copy
import pprint
import sys

N = int(input())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# pprint.pprint(board)


def print_board(board):
    for line in board:
        print(line)
    print()


def left(board):
    for i in range(N):
        cursor = 0
        for j in range(N):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0

                if board[i][cursor] == 0:
                    board[i][cursor] = temp

                elif board[i][cursor] == temp:
                    board[i][cursor] = temp * 2
                    cursor += 1

                elif board[i][cursor] != temp:
                    cursor += 1
                    board[i][cursor] = temp
    return board;


def right(board):
    for i in range(N):
        cursor = N - 1
        for j in range(N - 1, -1, -1):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0

                if board[i][cursor] == 0:
                    board[i][cursor] = temp

                elif board[i][cursor] == temp:
                    board[i][cursor] = temp * 2
                    cursor -= 1

                elif board[i][cursor] != temp:
                    cursor -= 1
                    board[i][cursor] = temp
    return board;


def up(board):
    for j in range(N):
        cursor = 0
        for i in range(N):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0

                if board[cursor][j] == 0:
                    board[cursor][j] = temp

                elif board[cursor][j] == temp:
                    board[cursor][j] = temp * 2
                    cursor += 1

                elif board[cursor][j] != temp:
                    cursor += 1
                    board[cursor][j] = temp
    return board;


def down(board):
    for j in range(N):
        cursor = N - 1
        for i in range(N - 1, -1, -1):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0

                if board[cursor][j] == 0:
                    board[cursor][j] = temp

                elif board[cursor][j] == temp:
                    board[cursor][j] = temp * 2
                    cursor -= 1

                elif board[cursor][j] != temp:
                    cursor -= 1
                    board[cursor][j] = temp
    return board;


Max = -1


def dfs(depth, arr):
    global Max

    if depth == 5:
        # 가장 큰 블록 프린트
        for i in range(N):
            for j in range(N):
                Max = max(Max, arr[i][j])
        return

    for i in range(4):
        copy_arr = copy.deepcopy(arr)
        if i == 0:
            dfs(depth + 1, left(copy_arr))
        elif i == 1:
            dfs(depth + 1, right(copy_arr))
        elif i == 2:
            dfs(depth + 1, up(copy_arr))
        else:
            dfs(depth + 1, down(copy_arr))


dfs(0, board)
print(Max)

#
# def dfs(dir, board, depth):
#     global Max
#     updated_board = copy.deepcopy(board)
#
#     if depth <= 5:
#         copy_board = copy.deepcopy(board)
#         if dir == 0:
#             updated_board = copy.deepcopy(up(copy_board))
#         elif dir == 1:
#             updated_board = copy.deepcopy(right(copy_board))
#         elif dir == 2:
#             updated_board = copy.deepcopy(down(copy_board))
#         elif dir == 3:
#             updated_board = copy.deepcopy(left(copy_board))
#
#     if depth == 5:
#         local_max = -1
#         # 가장 큰 블록 프린트
#         for i in range(N):
#             for j in range(N):
#                 local_max = max(local_max, updated_board[i][j])
#         Max = max(Max, local_max)
#         return
#
#     for d in range(4):
#         dfs(d, updated_board, depth + 1)
#
#
# dfs(-1, board, 0)
# print(Max)
