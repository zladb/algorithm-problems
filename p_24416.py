# 24416 - 알고리즘 수업 - 피보나치 수 1

n = int(input())

cnt1 = 0
cnt2 = 0


def fib(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    global cnt2
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        cnt2 += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


f = [0 for _ in range(41)]

fib(n)
fibonacci(n)

print(cnt1, cnt2)
