# 2439 - 별 찍기 -2

N = int(input())

for i in range(1, N+1):
    line = ''
    for j in range(1, i+1):
        line += '*'
    print(line.rjust(N, " "))
