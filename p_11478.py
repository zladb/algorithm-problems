# 11478 - 서로 다른 부분 문자열 개수

string = input()
ans = set()

size = 1
for size in range(1, len(string)+1):
    for i in range(0, len(string)-size+1):
        ans.add(string[i:i+size])

print(len(ans))
