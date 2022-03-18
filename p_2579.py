# 2579 - 계단 오르기

x = int(input())

stair = [0]
for _ in range(x):
    stair.append(int(input()))

if x == 1:
    print(stair[1])

else:
    dp = [0]*(x+1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]

    for i in range(3, x+1):
        dp[i] = max((dp[i - 3] + stair[i - 1] + stair[i]), dp[i - 2] + stair[i])

    print(dp[x])
