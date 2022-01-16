# 9663 - N-Queen

def is_promising(row, col, sol):

    for step in range(1, row):
        if row-step > 0:
            if 0 < col-step:
                if sol[row-step][col-step] == 1:
                    return False
            if sol[row-step][col] == 1:
                return False
            if col+step < N:
                if sol[row-step][col+step] == 1:
                    return False

    return True


def dfs(i):
    if i == N-1:
        global count
        count += 1
        return 0
    else:
        for j in range(1, N):
            if is_promising(i+1, j, sol):
                sol[i+1][j] = 1
                dfs(i+1)
                sol[i+1][j] = 0


N = int(input())
N += 1
count = 0
sol = [[0] * N for i in range(N)]
dfs(0)

print(count)
