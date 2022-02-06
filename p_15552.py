# 15552 - 빠른 A+B

import sys

T = int(input())
while T:
    num = list(map(int, sys.stdin.readline().rstrip().split()))
    print(num[0]+num[1])
    T -= 1
