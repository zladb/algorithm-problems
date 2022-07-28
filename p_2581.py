# 2581 - 소수

n = int(input())
m = int(input())

prime = []

for i in range(n, m + 1):
    for j in range(2, i + 1):
        if i % j == 0:
            if i == j:
                prime.append(i)
            else:
                break

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
