x = input()
x2 = input()
x3 = int(input())

x4 = 0

if x2 == 'small':
    if x == 'Watermelon':
        x4 = x3 * 2 * 56
    elif x == 'Mango':
        x4 = x3 * 2 * 36.66
    elif x == 'Pineapple':
        x4 = x3 * 2 * 42.10
    elif x == 'Raspberry':
        x4 = x3 * 2 * 20

elif x2 == 'big':
    if x == 'Watermelon':
        x4 = x3 * 5 * 28.70
    elif x == 'Mango':
        x4 = x3 * 5 * 19.60
    elif x == 'Pineapple':
        x4 = x3 * 5 * 24.80
    elif x == 'Raspberry':
        x4 = x3 * 5 * 15.20

if 400 <= x4 <= 1000:
    x4 = x4 * 0.85
elif x4 > 1000:
    x4 = x4 * 0.5

print(f'{x4:.02f} lv.')
