# 1436 - 영화감독 숌

n = int(input())

devil_number = '666'
number_set = set()

space = 4

for i in range(space, -1, -1):
    left = i
    right = space-i

    for left_num in range(0, 10**left):
        if right == 0:
            num = str(left_num) + devil_number
            number_set.add(int(num))
        else:
            for right_num in range(0, 10**right):
                num = str(left_num) + devil_number + str(right_num).zfill(right)
                number_set.add(int(num))

result = list(number_set)
result.sort()
print(result[n-1])
