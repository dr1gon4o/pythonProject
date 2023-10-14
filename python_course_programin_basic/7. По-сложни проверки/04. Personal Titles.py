x = float(input())
x2 = input()

if x2 == 'm':
    if x >= 16:
        print('Mr.')
    else:
        print('Master')
elif x2 == 'f':
    if x >= 16:
        print('Ms.')
    else:
        print('Miss')
