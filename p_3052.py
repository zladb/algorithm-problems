# 3052 - 나머지

numbers = list()
remainder = set()

for _ in range(10):
    numbers.append(int(input()))

for num in numbers:
    remainder.add(num % 42)

print(len(remainder))
