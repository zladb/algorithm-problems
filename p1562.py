# 1562 계단 수


N = int(input())

dp = [[[0, 0, 0, 0] * 10] for _ in range(N + 1)]
for i in range(10):
    if i == 0:
        dp[1][i][1 << 0] = 1
    elif i == 9:
        dp[1][i][1 << 1] = 1
    else:
        dp[1][i][0] = 1

MOD = 1000000000

for i in range(2, N + 1):
    for j in range(10):
        for bit in range(3):
            if j == 0:
                dp[i][j][bit | (1 << 0)] = dp[i - 1][1][bit] % MOD
            elif j == 9:
                dp[i][j][bit | (1 << 1)] = dp[i - 1][8][bit] % MOD
            else:
                dp[i][j][bit] = (dp[i - 1][j - 1][bit] + dp[i - 1][j + 1][bit]) % MOD

result = 0
for last in range(10):
    result += (dp[N][last][3]) % MOD

print(result)
