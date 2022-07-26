# 11286 - 절댓값 힙

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
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(a), a))
