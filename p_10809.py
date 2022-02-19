# 10809 - 알파벳 찾기

S = list(input())
result = [-1 for i in range(26)]
cnt = 0

for c in S:
    asc = ord(c)
    if 97 <= asc <= 122:
        if result[asc-97] == -1:
            result[asc-97] = cnt
    cnt += 1

print(*result, sep=' ')
