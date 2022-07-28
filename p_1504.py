# 1504 - 특정한 최단 경로

import heapq

INF = int(1e9)
V, E = map(int, input().split())

graph = [[] for i in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

u, v = map(int, input().split())

# print(graph)


def dijkstra(graph, start):
    distance = [INF] * (V + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (distance[start], start))

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    return distance


ans = {u: dijkstra(graph, u), v: dijkstra(graph, v)}

dist = min(ans[u][1] + ans[u][v] + ans[v][V], ans[v][1] + ans[u][v] + ans[u][V])
if dist >= INF:
    print(-1)
else:
    print(dist)

