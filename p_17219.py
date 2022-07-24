# 17219 - 비밀번호 찾기

import sys

n, m = map(int, input().split())

password = {}
for _ in range(n):
    site, pw = sys.stdin.readline().split()
    password[site] = pw

for _ in range(m):
    site = sys.stdin.readline().strip()
    print(password[site])
