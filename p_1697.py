# 1697 - 숨바꼭질

from collections import deque

n, k = map(int, input().split())


def bfs(root):
    visited = {root: 0}
    queue = deque([root])

    while queue:
        num = queue.popleft()

        if num == k:
            print(visited[num])
            break

        if 2*num <= 100000:
            if 2*num not in visited:
                visited[2*num] = visited[num] + 1
                queue.append(2*num)

        if num - 1 >= 0:
            if num - 1 not in visited:
                visited[num-1] = visited[num] + 1
                queue.append(num-1)

        if num + 1 <= 100000:
            if num + 1 not in visited:
                visited[num+1] = visited[num] + 1
                queue.append(num+1)


bfs(n)
