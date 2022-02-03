# 9461 - 파도반 수열

T = int(input())

sol = [1, 1, 1, 2, 2]

def padovan(n):
    if len(sol) < n:
        for i in range(len(sol), n+1):
            sol.append(sol[i-1]+sol[i-5])

    print(sol[n-1])

while T:
    N = int(input())
    padovan(N)
    T -= 1
