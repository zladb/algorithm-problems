# 더하기 사이클

N = input()

s = list(map(int, N))

count = 0

while True:
    # 한 자리 숫자일 경우 앞에 0을 붙여준다.
    if len(s) == 1:
        s.insert(0, 0)

    temp = int(s[0] + s[1]) % 10
    s[0] = s[1]
    s[1] = temp
    count += 1

    new = str(s[0])+str(s[1])
    if int(new) == int(N):
        break

print(count)
