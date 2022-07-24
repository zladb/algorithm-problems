# 2920 - 음계

music = list(map(int, input().split()))

ascending = 0
descending = 0
mixed = 0

if music[0] < music[1]:
    ascending = 1
elif music[0] > music[1]:
    descending = 1

for i in range(2, 8):
    if ascending:
        if music[i - 1] > music[i]:
            print('mixed')
            ascending = 0
            break
    elif descending:
        if music[i - 1] < music[i]:
            print('mixed')
            descending = 0
            break

if ascending == 1:
    print('ascending')
elif descending == 1:
    print('descending')
