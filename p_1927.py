# 1927 - 최소 힙

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
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, a)
