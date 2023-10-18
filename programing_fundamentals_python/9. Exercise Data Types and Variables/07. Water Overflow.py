n = int(input())

tank = 0
#tank = 255 litres
for l in range(n):
    litre = int(input())

    if (tank + litre) <= 255:
        tank += litre
    elif (tank + litre) >= 255:
        print("Insufficient capacity!")
    else:
        tank += litre

print(tank)
