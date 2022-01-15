# 15652 N과 M (4)

def dfs():
    if len(sol) == M:
        print(*sol, sep=' ')
        return 0
    else:
        for i in range(1, N + 1):
            if len(sol) == 0 or sol[-1] <= i:
                sol.append(i)
                dfs()
                sol.pop()


N, M = map(int, input().split())
sol = list()
dfs()
