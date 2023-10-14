x = input()
x2 = int(input())
x3 = int(input())

x4 = 0

if x == 'Roses':
    x4 = x2 * 5
    if x2 > 80:
        x4 = x4 - (x4 * 0.1)
elif x == 'Dahlias':
    x4 = x2 * 3.80
    if x2 > 90:
        x4 = x4 - (x4 * 0.15)
elif x == 'Tulips':
    x4 = x2 * 2.80
    if x2 > 80:
        x4 = x4 - (x4 * 0.15)
elif x == 'Narcissus':
    x4 = x2 * 3
    if x2 < 120:
        x4 = x4 + (x4 * 0.15)
elif x == 'Gladiolus':
    x4 = x2 * 2.50
    if x2 < 80:
        x4 = x4 + (x4 * 0.2)

if x3 >= x4:
    print(f"Hey, you have a great garden with {x2} {x} and {x3 -x4:.02f} leva left.")
else:
    print(f"Not enough money, you need {x4 - x3:.02f} leva more.")
