# 1269 - 대칭 차집합

n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len((A - B)) + len((B - A)))
