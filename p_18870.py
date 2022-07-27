# 18870 - 좌표 압축

import sys
import heapq

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
heap = list(set(nums))
heapq.heapify(heap)

ans = {}

for i in range(len(heap)):
    ans[heapq.heappop(heap)] = i

for number in nums:
    print(ans[number], end=' ')
