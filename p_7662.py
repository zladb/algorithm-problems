# 7662 - 이중 우선순위 큐

import heapq
import sys

T = int(input())

for _ in range(T):
    n = int(input())
    max_heap = []
    min_heap = []
    cnt = {}

    def clear(heap, k=1):
        while heap and not cnt[heap[0] * k]:
            heapq.heappop(heap)

    for _ in range(n):
        a = sys.stdin.readline().split()
        command, num = a[0], int(a[1])

        if command == 'I':
            heapq.heappush(max_heap, (-1) * num)
            heapq.heappush(min_heap, num)
            if num not in cnt:
                cnt[num] = 1
            else:
                cnt[num] += 1

        if command == 'D':
            if num == 1:
                clear(max_heap, -1)
                if not max_heap:
                    continue
                cnt[-max_heap[0]] -= 1
                if not cnt[-max_heap[0]]:
                    heapq.heappop(max_heap)

            elif num == -1:
                clear(min_heap)
                if not min_heap:
                    continue
                cnt[min_heap[0]] -= 1
                if not cnt[min_heap[0]]:
                    heapq.heappop(min_heap)



    clear(min_heap)
    clear(max_heap, -1)

    if min_heap and max_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print('EMPTY')
