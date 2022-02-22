# 2675 - 문자열 반복

T = int(input())

while T:
    t = list(input().split())
    for char in t[1]:
        for _ in range(int(t[0])):
            print(char, end='')
    print()
    T -= 1
