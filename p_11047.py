# 11047 - 동전 0

N, K = map(int, input().split())

coins = list()

for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)
count = 0

for coin in coins:
    while K-coin >= 0:
        K -= coin
        count += 1

print(count)
