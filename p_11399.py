# 11399 - ATM

N = int(input())
task = list(map(int, input().split()))


tast_time = 0
total = 0

for _ in range(N):
    fast_task = min(task)
    tast_time += fast_task
    task.remove(fast_task)
    total += tast_time

print(total)
