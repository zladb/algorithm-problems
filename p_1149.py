# 1149 - RGB 거리

n = int(input())

cost = list()
for _ in range(n):
    cost.append(list(map(int, input().split())))

for i in range(1, n):
    temp = cost[i].copy()
    for color in range(3):
        min_list = cost[i-1].copy()
        min_list.pop(color)
        min_value = min(min_list)
        temp[color] += min_value

    cost[i][:] = temp

print(min(temp))
