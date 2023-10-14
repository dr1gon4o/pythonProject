x = input()
x2 = input()
x3 = float(input())

if x2 == 'Monday' or x2 == 'Tuesday' or x2 == 'Wednesday' or x2 == 'Thursday' or x2 == 'Friday':
    if x == ('banana'):
        print(f'{x3 * 2.50:.02f}')
    elif x == ('apple'):
        print(f'{x3 * 1.20:.02f}')
    elif x == ('orange'):
        print(f'{x3 * 0.85:.02f}')
    elif x == ('grapefruit'):
        print(f'{x3 * 1.45:.02f}')
    elif x == ('kiwi'):
        print(f'{x3 * 2.70:.02f}')
    elif x == ('pineapple'):
        print(f'{x3 * 5.50:.02f}')
    elif x == ('grapes'):
        print(f'{x3 * 3.85:.02f}')
    else:
        print('error')
elif x2 == 'Saturday' or x2 == 'Sunday':
    if x == ('banana'):
        print(f'{x3 * 2.70:.02f}')
    elif x == ('apple'):
        print(f'{x3 * 1.25:.02f}')
    elif x == ('orange'):
        print(f'{x3 * 0.90:.02f}')
    elif x == ('grapefruit'):
        print(f'{x3 * 1.60:.02f}')
    elif x == ('kiwi'):
        print(f'{x3 * 3.00:.02f}')
    elif x == ('pineapple'):
        print(f'{x3 * 5.60:.02f}')
    elif x == ('grapes'):
        print(f'{x3 * 4.20:.02f}')
    else:
        print('error')
else:
    print('error')
