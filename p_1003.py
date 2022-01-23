# 1003 - 피보나치 함수

def fibonacci(n):
    if len(zero) != n+1:
        for i in range(3, n + 1):
            if len(zero) == i:
                zero.append(zero[i - 1] + zero[i - 2])
                one.append(one[i - 1] + one[i - 2])

    print('{0} {1}'.format(zero[n], one[n]))


zero = [1, 0, 1]
one = [0, 1, 1]

T = int(input())
for _ in range(T):
    n = int(input())
    fibonacci(n)
