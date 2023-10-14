x = input()
x2 = float(input())

if x == 'Sofia':
    if 0 <= x2 <= 500:
        print(f'{x2 * 0.05:.02f}')
    elif 500 < x2 <= 1000:
        print(f'{x2 * 0.07:.02f}')
    elif 1000 < x2 <= 10000:
        print(f'{x2 * 0.08:.02f}')
    elif x2 > 10000:
        print(f'{x2 * 0.12:.02f}')
    else:
        print('error')
elif x == 'Varna':
    if 0 <= x2 <= 500:
        print(f'{x2 * 0.045:.02f}')
    elif 500 < x2 <= 1000:
        print(f'{x2 * 0.075:.02f}')
    elif 1000 < x2 <= 10000:
        print(f'{x2 * 0.1:.02f}')
    elif x2 > 10000:
        print(f'{x2 * 0.13:.02f}')
    else:
        print('error')
elif x == 'Plovdiv':
    if 0 <= x2 <= 500:
        print(f'{x2 * 0.055:.02f}')
    elif 500 < x2 <= 1000:
        print(f'{x2 * 0.08:.02f}')
    elif 1000 < x2 <= 10000:
        print(f'{x2 * 0.12:.02f}')
    elif x2 > 10000:
        print(f'{x2 * 0.145:.02f}')
    else:
        print('error')
else:
    print('error')
