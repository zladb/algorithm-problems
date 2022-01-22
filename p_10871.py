# 10871 - X보다 작은 수

N, X = map(int, input().split())

num = [int(x) for x in input().split()]

for number in num:
    if number < X:
        print(number, end=' ')
