# 2660 - 회장뽑기

from collections import deque

n = int(input())

friend = {}

while True:
    a, b = map(int, input().split())

    if a == -1 and b == -1:
        break

    if a not in friend:
        friend[a] = [b]
    else:
        friend[a].append(b)

    if b not in friend:
        friend[b] = [a]
    else:
        friend[b].append(a)

# print(friend)

score = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    score[i][i] = -1
    score[i][0] = -1


# print(score)


def bfs(root):
    visited = []
    queue = deque([(root, 0)])

    while queue:
        person, level = queue.popleft()
        if person not in visited:
            if person != root:
                score[root][person] = level
            visited.append(person)
            for p in range(len(friend[person])):
                queue.append((friend[person][p], level + 1))


candidate = {}

for i in range(1, n + 1):
    bfs(i)
    # print(*score[i], sep=' ')
    if 0 not in score[i]:
        candidate[i] = max(score[i])

temp = list(candidate.values())
minimum = min(temp)
count = temp.count(minimum)
print(minimum, count)

for k, v in candidate.items():
    if v == minimum:
        print(k, end=' ')
