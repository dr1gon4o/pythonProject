x = float(input())
x2 = input()
x3 = int(input())
x4 = input()

x5 = 0

if x2 == "m":
    if x4 == 'Gym':
        x5 = 42
    elif x4 == 'Boxing':
        x5 = 41
    elif x4 == 'Yoga':
        x5 = 45
    elif x4 == 'Zumba':
        x5 = 34
    elif x4 == 'Dances':
        x5 = 51
    elif x4 == 'Pilates':
        x5 = 39
elif x2 == "f":
    if x4 == 'Gym':
        x5 = 35
    elif x4 == 'Boxing':
        x5 = 37
    elif x4 == 'Yoga':
        x5 = 42
    elif x4 == 'Zumba':
        x5 = 31
    elif x4 == 'Dances':
        x5 = 53
    elif x4 == 'Pilates':
        x5 = 37

if x3 <= 19:
    x5 = x5 * 0.8

if x >= x5:
    print(f"You purchased a 1 month pass for {x4}.")
else:
    print(f"You don't have enough money! You need ${x5 - x:.02f} more.")
