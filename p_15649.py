# 15649 N과 M (1)

N, M = map(int, input().split())
sol = list()


def dfs():
    if len(sol) == M:
        print(*sol, sep=' ')
        return 0
    else:
        for i in range(1, N + 1):
            if i not in sol:
                sol.append(i)
                dfs()
                sol.pop()


dfs()
