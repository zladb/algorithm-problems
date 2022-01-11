# 2884 - 알람 시계

H, M = map(int, input().split())

alarm_H = 0
alarm_M = 0


if M >= 45:
    alarm_H = H
    alarm_M = M - 45

else:
    if H == 0:
        alarm_H = 23
    else:
        alarm_H = H - 1
    alarm_M = 60 + (M - 45)

print(alarm_H, alarm_M, sep=' ')
