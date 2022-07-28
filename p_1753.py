# 1753 - 최단경로

import heapq
INF = int(1e9)
V, E = map(int, input().split())
K = int(input())
graph = {}

# for _ in range(E):
#     u, v, w = map(int, input().split())
#     if u not in graph:
#         graph.update({u: {v: w}})
#     else:
#         graph[u].update({v: w})
#
# for i in range(1, V + 1):
#     if i not in graph:
#         graph[i] = {}

graph = [[] for i in range(V + 1)]
for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))

# print(graph)

distance = [INF] * (V + 1)


def dijkstra(graph, start):
    # distances = {node: INF for node in graph}
    # distances[start] = 0
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (distance[start], start))

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        # for new_destination, new_distance in graph[now].items():
        #     cost = dist + new_distance
        #     if cost < distance[new_destination]:
        #         distance[new_destination] = cost
        #         heapq.heappush(queue, (cost, new_destination))

        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    # return distances


# ans = {}
# ans = dijkstra(graph, K)

# for i in range(1, V + 1):
#     if ans[i] == INF:
#         print('INF')
#     else:
#         print(ans[i])

dijkstra(graph, K)

for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])

