# 11021 A+B - 7

N = int(input())

for i in range(1, N+1):
    A, B = map(int, input().split())
    print(f"Case #{i}: {A+B}")
