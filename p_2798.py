# 2798 - 블랙잭

# 카드수 n (3<=n<=100), 숫자 m(10<=m<=300,000)
n, m = map(int, input().split())

card = list(map(int, input().split()))
# card = [int(x) for x in input().split()]
card.sort(reverse=True)

card_sum = 0
max_sum = 0
index = 0

for i in range(0, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            card_sum = card[i] + card[j] + card[k]
            if (card_sum <= m) and (card_sum > max_sum):
                max_sum = card_sum

print(max_sum)
