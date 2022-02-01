# 1932 - 정수 삼각형

n = int(input())
tri = list()

for i in range(n):
    tri.append(list(map(int, input().split())))

for i in range(n-2, -1, -1):
    for j in range(len(tri[i])):
        if tri[i][j] + tri[i+1][j] >= tri[i][j] + tri[i+1][j+1]:
            tri[i][j] += tri[i+1][j]
        else:
            tri[i][j] += tri[i+1][j+1]

print(tri[i][j])
