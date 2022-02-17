# 4344 - 평균은 넘겠지

C = int(input())

while C:
    info = list(map(int, input().split()))
    n = info[0]
    scores = info[1:]
    aver = sum(scores)//n
    cnt = 0
    for score in scores:
        if score > aver:
            cnt += 1
    print("%.3f%%" % (cnt/n * 100.0))
    C -= 1
