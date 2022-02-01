# 1149 - RGB 거리

from pprint import pprint

n = int(input())

cost = list()
for _ in range(n):
    cost.append(list(map(int, input().split())))

pprint(cost)
