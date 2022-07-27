# 1620 - 나는야 포켓몬 마스터 이다솜

n, m = map(int, input().split())

pokemon_list = [0]
pokemon_dict = {}

for i in range(n):
    pokemon = input()
    pokemon_list.append(pokemon)
    pokemon_dict[pokemon] = i + 1

for _ in range(m):
    a = input()
    if a.isdigit():
        print(pokemon_list[int(a)])
    else:
        print(pokemon_dict[a])
