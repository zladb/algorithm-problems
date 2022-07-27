# 9095 - 1, 2, 3 더하기

T = int(input())
f = [1, 2, 4]

for _ in range(T):
    n = int(input())

    if len(f) <= n:
        for i in range(len(f), n + 1):
            f.append(f[i-3]+f[i-2]+f[i-1])
    print(f[n-1])
