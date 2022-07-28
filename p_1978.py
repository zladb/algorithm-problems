# 1978 - 소수 찾기

n = int(input())

nums = map(int, input().split())

cnt = 0
for n in nums:
    for i in range(2, n + 1):
        if n % i == 0:
            if i == n:
                cnt += 1
            else:
                break

print(cnt)
