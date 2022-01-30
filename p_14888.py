# 14888 - 연산자 끼워넣기

N = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))

num_len = len(numbers)
operator_len = num_len - 1

expression = list()
sol = list()

def dfs(i, val):
    expression.append(str(numbers[i]))

    if i != 0:
        # 음수를 나누는 경우
        if val < 0 and expression[-2] == '//':
            val = -((-val) // int(expression[-1]))
        else:
            exp = str(val) + ''.join(expression[-2:])
            val = eval(exp)

    # 식을 완성한 경우
    if len(expression) == num_len + operator_len:
        sol.append(val)
        return

    else:
        for j in range(0, 4):
            if operator[j] != 0:
                if j == 0:
                    expression.append('+')
                elif j == 1:
                    expression.append('-')
                elif j == 2:
                    expression.append('*')
                else:
                    expression.append('//')

                operator[j] -= 1
                dfs(i + 1, val)
                expression.pop()
                expression.pop()
                operator[j] += 1


dfs(0, numbers[0])
print(max(sol))
print(min(sol))
