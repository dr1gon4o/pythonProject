line = input()

haha = {}
while line != "buy":
    hoho = line.split()
    k = hoho[0]
    # v = float(hoho[1])
    # f = float(hoho[2])
    if k not in haha:
        haha[k] = {}
        v, f = float(hoho[1]), float(hoho[2])
        # v = float(hoho[1])
        # f = float(hoho[2])
        haha[k][v] = f

    else:
        h, g = float(hoho[1]), float(hoho[2])
        popo = 0
        for x, i in haha.items():
            if k == x:
                for t, y in i.items():
                    popo += g + y
                    haha[x][t] = popo
        if k in haha.keys():
            lulu = {h: popo}
            haha[k].update(lulu)

    line = input()

list = {}
for x, y in haha.items():
    for o, i in y.items():
        pupu = o * i
        print(f'{x} -> {pupu:.02f}')

print(line)
print(haha)

