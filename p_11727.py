# 11727 - 2xn 타일링 2

n = int(input())

f = [1, 3]
for i in range(2, n):
    f.append(f[i - 1] + f[i - 2] * 2)

print(f[n - 1]%10007)
