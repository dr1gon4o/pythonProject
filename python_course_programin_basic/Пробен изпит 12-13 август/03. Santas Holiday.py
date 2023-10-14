x = int(input())
x2 = input()
x3 = input()

cena = 0
x4 = 0

if x2 == "room for one person":
    cena = (x - 1) * 18
    x4 = cena
elif x2 == "apartment":
    cena = (x - 1) * 25
    if x < 10:
        x4 = cena * 0.7
    elif 10 <= x <= 15:
        x4 = cena * 0.65
    elif x > 15:
        x4 = cena * 0.5
elif x2 == "president apartment":
    cena = (x - 1) * 35
    if x < 10:
        x4 = cena * 0.9
    elif 10 <= x <= 15:
        x4 = cena * 0.85
    elif x > 15:
        x4 = cena * 0.8

x5 = 0

if x3 == "positive":
    x5 = x4 + (x4 * 0.25)
elif x3 == "negative":
    x5 = x4 - (x4 * 0.1)

print(f'{x5:.02f}')
