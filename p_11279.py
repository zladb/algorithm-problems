# 11279 - 최대 힙

import sys
import heapq

n = int(input())
heap = []

for _ in range(n):
    a = int(sys.stdin.readline().strip())

    if a == 0:
        if len(heap) == 0:
            print(0)
        else:
            print((-1)*heapq.heappop(heap))
    else:
        heapq.heappush(heap, (-1)*a)
