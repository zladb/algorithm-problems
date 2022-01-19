# 9663 - N-Queen

def is_promising(sol, row, col):

    for index in range(1, row):
        if sol[index] == col or abs(index - row) == abs(sol[index] - col):
            return False
    return True


def dfs(row):
    if row == N:
        global count
        count += 1
    else:

        for col in range(1, N+1):   # 1 ~ N
            if row == 0:
                if N % 2 == 0 and row > N//2:
                    break
                sol[row + 1] = col
                dfs(row + 1)
                sol[row + 1] = 0

            elif is_promising(sol, row+1, col):
                sol[row + 1] = col
                dfs(row + 1)
                sol[row + 1] = 0


N = int(input())
count = 0
sol = [0] * (N+1)
dfs(0)

if N % 2 == 0:
    print(count*2)
else:
    print(count)
