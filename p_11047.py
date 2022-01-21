# 11047 - 동전 0

N, K = map(int, input().split())

coins = list()

for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)
print(coins)
count = 0

while True:
    for coin in coins:
        if K >= coin:
            K -= coin
            count += 1
            break
        else:  # K < coin
            print(coins)
            coins.remove(coin)
            print(K)
            print(coins)
            print()

    if K == 0:
        break

print(count)
