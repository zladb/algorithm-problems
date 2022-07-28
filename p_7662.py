# 7662 - 이중 우선순위 큐

import heapq
import sys

heap = []
cnt = {}

T = int(input())

for _ in range(T):
    n = int(input())

    for _ in range(n):
        a = sys.stdin.readline().split()
        command, num = a[0], int(a[1])

        if command == 'I':
            heapq.heappush(heap, num)

        if command == 'D':
            if len(heap) > 0:
                if num == 1:
                    heap = heapq.nlargest(len(heap), heap)[1:]
                    heapq.heapify(heap)
                elif num == -1:
                    heapq.heappop(heap)

    if len(heap) == 0:
        print('EMPTY')
    else:
        # print(heapq.nlargest(1,heap)[0], heap)
        print(max(heap), min(heap))
