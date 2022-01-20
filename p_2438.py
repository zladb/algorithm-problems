# 2438 별 찍기 - 1

N = int(input())

for i in range(1, N+1):
    for j in range(1, i+1):
        print("*", end='')
    print()
