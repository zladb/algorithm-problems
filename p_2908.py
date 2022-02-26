# 2908 - 상수

A, B = map(list, input().split())
A.reverse()
B.reverse()

a = ''.join(A)
b = ''.join(B)

if int(a) > int(b):
    print(a)
else:
    print(b)
