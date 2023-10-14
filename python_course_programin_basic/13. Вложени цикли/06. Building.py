x = int(input())
x2 = int(input())


for etaj in reversed(range(1, x + 1)):

    if etaj % 2:
        duma = 'A'
    else:
        duma = 'O'

    if etaj == x:
        duma = 'L'

    for office in range(x2):
        ime_etaj = f"{duma}{etaj}{office}"
        print(ime_etaj, end=' ')

    print()
