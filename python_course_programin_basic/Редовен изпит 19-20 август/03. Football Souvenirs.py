x1 = input()
x2 = input()
x3 = int(input())

all = 0

popo = False

if x1 == 'Argentina':
    if x2 == 'flags':
        popo = True
        all += x3 * 3.25
    elif x2 == 'caps':
        popo = True
        all += x3 * 7.20
    elif x2 == 'posters':
        popo = True
        all += x3 * 5.10
    elif x2 == 'stickers':
        popo = True
        all += x3 * 1.25
    else:
        print("Invalid stock!")

elif x1 == 'Brazil':
    if x2 == 'flags':
        popo = True
        all += x3 * 4.20
    elif x2 == 'caps':
        popo = True
        all += x3 * 8.50
    elif x2 == 'posters':
        popo = True
        all += x3 * 5.35
    elif x2 == 'stickers':
        popo = True
        all += x3 * 1.20
    else:
        print("Invalid stock!")

elif x1 == 'Croatia':
    if x2 == 'flags':
        popo = True
        all += x3 * 2.75
    elif x2 == 'caps':
        popo = True
        all += x3 * 6.90
    elif x2 == 'posters':
        popo = True
        all += x3 * 4.95
    elif x2 == 'stickers':
        popo = True
        all += x3 * 1.10
    else:
        print("Invalid stock!")

elif x1 == 'Denmark':
    if x2 == 'flags':
        popo = True
        all += x3 * 3.10
    elif x2 == 'caps':
        popo = True
        all += x3 * 6.50
    elif x2 == 'posters':
        popo = True
        all += x3 * 4.80
    elif x2 == 'stickers':
        popo = True
        all += x3 * 0.90
    else:
        print("Invalid stock!")

else:
    print("Invalid country!")


if popo:
    print(f'Pepi bought {x3} {x2} of {x1} for {all:.02f} lv.')

