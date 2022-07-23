# 2667 - 단지번호붙이기

n = int(input())

smap = []

for _ in range(n):
    line = list(input())
    smap.append(line)


def dfs(x, y):

    stack = set()
    stack.add((x, y))

    cnt = 0

    while stack:
        spot = stack.pop()
        x, y = spot[0], spot[1]
        if smap[x][y] == '1':
            cnt += 1
            smap[x][y] = '0'

        #
            if x+1 < n:
                stack.add((x+1, y))
            if x-1 >= 0:
                stack.add((x - 1, y))
            if y+1 < n:
                stack.add((x, y+1))
            if y-1 >= 0:
                stack.add((x, y-1))

    return cnt


answer = []

for row in range(n):
    for col in range(n):
        if smap[row][col] == '1':
            answer.append(dfs(row, col))

answer.sort()
print(len(answer))
print(*answer, sep='\n')
