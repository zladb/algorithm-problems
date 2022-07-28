# 1912 - 연속합

import sys

n = int(input())

nums = list(map(int, sys.stdin.readline().split()))

ans = []
sum_part = 0
for k in nums:
    sum_part += k
    if sum_part >= k:
        ans.append(sum_part)
    else:
        ans.append(k)
        sum_part = k

print(max(ans))
