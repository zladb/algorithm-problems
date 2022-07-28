# 7662 - 이중 우선순위 큐

import heapq

max_heap = []
min_heap = []
cnt = {}

T = int(input())

for _ in range(T):
    n = int(input())

    for _ in range(n):
        a = input().split()
        command, num = a[0], int(a[1])

        if command == 'I':
            heapq.heappush(max_heap, (-1) * num)
            heapq.heappush(min_heap, num)
            if num not in cnt:
                cnt[num] = 1
            else:
                cnt[num] += 1

            # print(max_heap, sep=' ')
            # print(min_heap, sep=' ')
            # print(cnt)
            # print()

        if command == 'D':
            if num == 1:
                while len(max_heap):
                    d = (-1) * max_heap[0]
                    heapq.heappop(max_heap)
                    if cnt[d] == 0:
                        del cnt[d]
                    elif cnt[d] > 0:
                        cnt[d] -= 1
                        break
            elif num == -1:
                while len(min_heap):
                    d = min_heap[0]
                    heapq.heappop(min_heap)
                    if cnt[d] == 0:
                        del cnt[d]
                    elif cnt[d] > 0:
                        cnt[d] -= 1
                        break

            # print(max_heap, sep=' ')
            # print(min_heap, sep=' ')
            # print(cnt)
            # print()

    empty = True
    for check in cnt.values():
        if check != 0:
            empty = False

    if empty:
        print('EMPTY')
    else:
        for maxi in max_heap:
            if cnt[(-1)*maxi] == 0:
                del max_heap[maxi]
                max_heap.pop(0)
            else:
                _max = (-1) * max_heap[0]
                break

        for mini in min_heap:
            if cnt[mini] == 0:
                del min_heap[mini]
                min_heap.pop(0)
            else:
                _min = min_heap[0]
                break
        # # _max = (-1) * max_heap[0]
        # # _min = min_heap[0]
        # print(cnt)
        # print(min_heap)
        # print(max_heap)
        print(_max, _min)
