# 8958 - OX퀴즈

def score():
    total = 0
    cnt = 0
    for result in quiz:
        if result == 'O':
            cnt += 1
            total += cnt
        elif result == 'X':
            cnt = 0
    print(total)


T = int(input())
quiz = list()

while T:
    quiz = list(input())
    score()
    quiz.clear()
    T -= 1
