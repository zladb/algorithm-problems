# 1546 - 평균

N = int(input())

score = list(map(int, input().split()))
new_score = list()

M = max(score)
for s in score:
    new_score.append(s/M*100)

print(sum(new_score)/N)
