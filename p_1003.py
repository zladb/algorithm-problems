# 1003 - 피보나치 함수

def fibonacci(n):

    if n <= 2:
        return n

    for i in range (n):
        




zero = [1, 0, 1]
one = [0, 1, 1]

T = int(input())
for _ in range(T):
    count_zero = 0
    count_one = 0
    n = int(input())
    fibonacci(n)
    print(count_zero, count_one, sep=' ')
