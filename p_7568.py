# 7568 - 덩치

# 사람수 n(2<=n<=50)
n = int(input())

# 사람 입력
people = []
for _ in range(n):
    weight, height = map(int, input().split())
    people.append((weight, height))

for person in people:
    rank = 1
    for another_person in people:
        if person[0] < another_person[0] and person[1] < another_person[1]:
            rank += 1
    print(rank, end=' ')
