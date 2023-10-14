x = int(input())
x2 = input()

suma = 0

if x2 == 'spring':
    if x <= 5:
        suma = x * 50
    else:
        suma = x * 48
elif x2 == 'summer':
    if x <= 5:
        suma = x * 48.5
    else:
        suma = x * 45
elif x2 == 'autumn':
    if x <= 5:
        suma = x * 60
    else:
        suma = x * 49.5
elif x2 == 'winter':
    if x <= 5:
        suma = x * 86
    else:
        suma = x * 85

if x2 == 'summer':
    suma = suma * 0.85
elif x2 == 'winter':
    suma = suma + (suma * 0.08)

print(f"{suma:.02f} leva.")
