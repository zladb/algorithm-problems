# 2588
a = int(input())
b = int(input())
first = a * (b % 10)
second = a * (b % 100 // 10)
third = a * (b // 100)
result = first + second*10 + third*100
print(first)
print(second)
print(third)
print(result)
