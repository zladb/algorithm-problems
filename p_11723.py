# 11723 - 집합

import sys

m = int(input())
S = set()

for _ in range(m):
    temp = sys.stdin.readline().strip().split()

    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()

    else:
        inst, x = temp[0], temp[1]
        value = int(x)

        if inst == 'add':
            S.add(value)

        elif inst == 'remove':
            S.discard(value)

        elif inst == 'check':
            print(1 if value in S else 0)

        elif inst == 'toggle':
            if value in S:
                S.discard(value)
            else:
                S.add(value)

