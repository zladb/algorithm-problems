# 나머지

numbers = list()
remainder = list()

for _ in range(10):
    numbers.append(int(input()))

for num in numbers:
    if num % 42 not in remainder:
        remainder.append(num % 42)

print(len(remainder))
