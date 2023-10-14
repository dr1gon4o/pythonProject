x = int(input())
x2 = input()
x3 = input()

x4 = 0

if x2 == 'room for one person':
    x4 = (x - 1) * 18

elif x2 == 'apartment':
    if x <= 10:
        x4 = (x - 1) * 0.7 * 25
    elif 10 < x <= 15:
        x4 = (x - 1) * 0.65 * 25
    else:
        x4 = (x - 1) * 0.5 * 25

elif x2 == 'president apartment':
    if x <= 10:
        x4 = (x - 1) * 0.9 * 35
    elif 10 < x <= 15:
        x4 = (x - 1) * 0.85 * 35
    else:
        x4 = (x - 1) * 0.8 * 35

if x3 == 'positive':
    x4 = x4 * 1.25
elif x3 == 'negative':
    x4 = x4 * 0.9

print(f'{x4:.02f}')
