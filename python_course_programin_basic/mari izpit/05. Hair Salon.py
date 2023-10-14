cel = int(input())
# x = input()
# x2 = input()

suma = 0

while True:
    x = input()
    if x == 'closed':
        break
    x2 = input()
    # x = input()
    # x2 = input()

    if x == 'haircut':
        if x2 == 'men':
            suma += 15
        elif x2 == 'ladies':
            suma += 20
        elif x2 == 'kids':
            suma += 10
    elif x == 'color':
        if x2 == 'touch up':
            suma += 20
        elif x2 == 'full color':
            suma += 30

    if suma >= cel:
        break

if suma >= cel:
    print("You have reached your target for the day!")
    print(f"Earned money: {suma}lv.")
else:
    print(f"Target not reached! You need {cel - suma}lv. more.")
    print(f"Earned money: {suma}lv.")


