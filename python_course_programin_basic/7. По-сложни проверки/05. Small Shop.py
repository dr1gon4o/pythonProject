x = input()
x2 = input()
x3 = float(input())

pr = 0

if x2 == 'Sofia':
    if x == 'coffee':
        pr = x3 * 0.50
    elif x == 'water':
        pr = x3 * 0.80
    elif x == 'beer':
        pr = x3 * 1.20
    elif x == 'sweets':
        pr = x3 * 1.45
    elif x == 'peanuts':
        pr = x3 * 1.60

elif x2 == 'Plovdiv':
    if x == 'coffee':
        pr = x3 * 0.40
    elif x == 'water':
        pr = x3 * 0.70
    elif x == 'beer':
        pr = x3 * 1.15
    elif x == 'sweets':
        pr = x3 * 1.30
    elif x == 'peanuts':
        pr = x3 * 1.50

elif x2 == 'Varna':
    if x == 'coffee':
        pr = x3 * 0.45
    elif x == 'water':
        pr = x3 * 0.70
    elif x == 'beer':
        pr = x3 * 1.10
    elif x == 'sweets':
        pr = x3 * 1.35
    elif x == 'peanuts':
        pr = x3 * 1.55

print(pr)
