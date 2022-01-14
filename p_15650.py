# 15649 N과 M (2)

def dfs():
    if len(sol) == M:
        sol_tu = tuple(sorted(sol))
        sol_set.add(sol_tu)
        return 0
    else:
        for i in range(1, N + 1):
            if i not in sol:
                sol.append(i)
                dfs()
                sol.pop()


N, M = map(int, input().split())
sol = list()
sol_set = set()
dfs()

output = sorted(list(sol_set))
for out in output:
    print(*out, sep=' ')
