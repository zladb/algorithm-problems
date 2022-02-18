# 2525 - 오븐 시계

H, M = map(int, input().split())
time = int(input())

M = M + time
while M >= 60:
    H += 1
    if H == 24:
        H = 0
    M -= 60

print(H, M)
