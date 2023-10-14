suma = float(input())

broi = 0

while True:
    # suma = float(input())

    if suma >= 2:
        suma -= 2
        broi += 1
        suma = round(suma, 2)

    elif suma >= 1:
        suma -= 1
        broi += 1
        suma = round(suma, 2)

    elif suma >= 0.5:
        suma -= 0.5
        broi += 1
        suma = round(suma, 2)

    elif suma >= 0.2:
        suma -= 0.2
        broi += 1
        suma = round(suma, 2)

    elif suma >= 0.1:
        suma -= 0.1
        broi += 1
        suma = round(suma, 2)

    elif suma >= 0.05:
        suma -= 0.05
        broi += 1
        suma = round(suma, 2)

    elif suma >= 0.02:
        suma -= 0.02
        broi += 1
        suma = round(suma, 2)

    elif suma >= 0.01:
        suma -= 0.01
        broi += 1
        suma = round(suma, 2)

    if suma == 0:
        break

print(broi)
