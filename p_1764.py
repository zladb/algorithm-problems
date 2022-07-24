# 1764 - 듣보잡

n, m = map(int, input().split())

d = set()
b = set()

for _ in range(n):
    d.add(input())

for _ in range(m):
    b.add(input())

ans = list(d & b)
ans.sort()
print(len(ans))
print(*ans, sep='\n')
