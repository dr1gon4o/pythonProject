x = int(input()) * 1000
xrana = input()

x2 = 0
# kg = x2 / 1000

while True:
    if xrana == 'Adopted':
        break

    xrana = int(xrana)
    x2 += xrana
    kg = x2 / 1000

    # if x >= x2:
    #     break
    xrana = input()

    #     print(f"Food is enough! Leftovers: {x - x2} grams.")
    # else:
    #     print(f"Food is not enough. You need {x2 - x} grams more.")

if x >= x2:
    print(f"Food is enough! Leftovers: {x - x2} grams.")
else:
    print(f"Food is not enough. You need {x2 - x} grams more.")
