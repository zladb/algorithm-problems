# 2480 - 주사위 세개

fir, sec, thd = map(int, input().split())

if fir == sec == thd:
    print(10000+fir*1000)

elif fir == sec or fir == thd:
    print(1000+fir*100)

elif sec == thd:
    print(1000+sec*100)

else:
    print(max(fir, sec, thd)*100)
