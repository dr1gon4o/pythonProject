x = int(input())
x2 = input()
x3 = int(input())

x4 = 0

if x2 == 'Spring':
    x4 = 3000
    if x3 <= 6:
        x4 = x4 - (x4 * 0.1)
    elif 7 <= x3 <= 11:
        x4 = x4 - (x4 * 0.15)
    elif x3 >= 12:
        x4 = x4 - (x4 * 0.25)

elif x2 == 'Summer':
    x4 = 4200
    if x3 <= 6:
        x4 = x4 - (x4 * 0.1)
    elif 7 <= x3 <= 11:
        x4 = x4 - (x4 * 0.15)
    elif x3 >= 12:
        x4 = x4 - (x4 * 0.25)

elif x2 == 'Autumn':
    x4 = 4200
    if x3 <= 6:
        x4 = x4 - (x4 * 0.1)
    elif 7 <= x3 <= 11:
        x4 = x4 - (x4 * 0.15)
    elif x3 >= 12:
        x4 = x4 - (x4 * 0.25)

elif x2 == 'Winter':
    x4 = 2600
    if x3 <= 6:
        x4 = x4 - (x4 * 0.1)
    elif 7 <= x3 <= 11:
        x4 = x4 - (x4 * 0.15)
    elif x3 >= 12:
        x4 = x4 - (x4 * 0.25)

if x3 % 2 == 0 and x2 != 'Autumn':
    x4 = x4 - (x4 * 0.05)

if x >= x4 and x:
    print(f"Yes! You have {x - x4:.02f} leva left.")
else:
    print(f"Not enough money! You need {x4 - x:.02f} leva.")
