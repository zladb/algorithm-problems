# 9184 - 신나는 함수 실행

def w(a, b, c):
    if (a, b, c) in answer.keys():
        return answer[(a, b, c)]

    if a <= 0 or b <= 0 or c <= 0:
        answer[(a, b, c)] = 1
        return answer[(a, b, c)]

    if a > 20 or b > 20 or c > 20:
        answer[(a, b, c)] = w(20, 20, 20)
        return answer[(a, b, c)]

    if a < b < c:
        answer[(a, b, c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return answer[(a, b, c)]

    else:  # 20 20 20
        answer[(a, b, c)] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return answer[(a, b, c)]


answer = dict()

while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (-1, -1, -1):
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
