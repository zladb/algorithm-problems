# 1904 - 01타일

def tile(n):
    if len(sol) < n:
        for i in range(len(sol), n + 1):
            sol.append((sol[i - 1] + sol[i - 2]) % 15746)

    print(sol[n - 1])


n = int(input())
sol = [1, 2]
tile(n)
