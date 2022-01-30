# 14888 - 연산자 끼워넣기

N = int(input())

numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))  # + - * /

print(numbers)
print(operator)

num_len = len(numbers)
operator_len = num_len - 1

expression = list()
sol = list()

def dfs(i):
    expression.append(str(numbers[i]))
    if len(expression) == num_len + operator_len:
        print(*expression, sep=' ')
        exp = ''.join(expression)
        print(eval(exp))
        sol.append(eval(exp))
        return 0
    else:
        for j in range(0, 4):
            if operator[j] != 0 and i + 1 != num_len:
                if j == 0:
                    expression.append('+')
                elif j == 1:
                    expression.append('-')
                elif j == 2:
                    expression.append('*')
                else:
                    expression.append('//')

                operator[j] -= 1
                dfs(i + 1)
                expression.pop()
                expression.pop()
                operator[j] += 1


dfs(0)
print(max(sol))
print(min(sol))
