x = int(input())
x2 = input()

x3 = 0
x4 = 0

if x2 == 'Morning':
    if 10 <= x <= 18:
        x3 = 'Sweatshirt'
        x4 = 'Sneakers'
    elif 18 < x <= 24:
        x3 = 'Shirt'
        x4 = 'Moccasins'
    elif x >= 25:
        x3 = 'T-Shirt'
        x4 = 'Sandals'
elif x2 == 'Afternoon':
    if 10 <= x <= 18:
        x3 = 'Shirt'
        x4 = 'Moccasins'
    elif 18 < x <= 24:
        x3 = 'T-Shirt'
        x4 = 'Sandals'
    elif x >= 25:
        x3 = 'Swim Suit'
        x4 = 'Barefoot'
elif x2 == 'Evening':
    if 10 <= x <= 18:
        x3 = 'Shirt'
        x4 = 'Moccasins'
    elif 18 < x <= 24:
        x3 = 'Shirt'
        x4 = 'Moccasins'
    elif x >= 25:
        x3 = 'Shirt'
        x4 = 'Moccasins'

print(f"It's {x} degrees, get your {x3} and {x4}.")
