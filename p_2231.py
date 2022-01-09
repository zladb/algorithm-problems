# 2231 - 분해합

# 자연수 n(1<=n<=1,000,000)
n = int(input())
result = 0

for i in range(1, n):
    str_num = list(str(i))
    elements = [int(x) for x in str_num]
    # print("elements : ", elements)
    분해합 = i + sum(elements)
    if 분해합 == n:
        result = i
        break

print(result)
