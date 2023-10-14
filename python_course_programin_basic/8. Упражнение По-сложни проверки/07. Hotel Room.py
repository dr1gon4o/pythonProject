import os

x = input()
x2 = int(input())

x3 = 0
x4 = 0

if x == 'May' or x == 'October':
    x3 = x2 * 50
    x4 = x2 * 65
    if 7 < x2 <= 14:
        x3 = x3 - (x3 * 0.05)
    elif x2 > 14:
        x3 = x3 - (x3 * 0.3)
        x4 = x4 - (x4 * 0.1)

elif x == 'June' or x == 'September':
    x3 = x2 * 75.20
    x4 = x2 * 68.70
    if x2 > 14:
        x3 = x3 - (x3 * 0.2)
        x4 = x4 - (x4 * 0.1)

elif x == 'July' or x == 'August':
    x3 = x2 * 76
    x4 = x2 * 77
    if x2 > 14:
        x4 = x4 - (x4 * 0.1)


print(f"Apartment: {x4:.02f} lv.", f"Studio: {x3:.02f} lv.", sep=os.linesep)
