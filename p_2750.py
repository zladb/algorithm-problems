# 2750 - 수 정렬하기

N = int(input())

nums = list()

for _ in range(N):
    nums.append(int(input()))

nums.sort()

for num in nums:
    print(num)
