x = input()
x2 = int(input())
x3 = int(input())

if x == 'Premiere':
    print(f'{x3 * x2 * 12.00:.02f} leva')

elif x == 'Normal':
    print(f'{x3 * x2 * 7.50:.02f} leva')

elif x == 'Discount':
    print(f'{x3 * x2 * 5.00:.02f} leva')
