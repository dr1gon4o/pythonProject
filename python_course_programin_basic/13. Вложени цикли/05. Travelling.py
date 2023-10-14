x = 0

while True:

    dest = input()

    if dest == "End":
        break

    suma = float(input())
    x = 0

    while x < suma:
        cena = float(input())
        x += cena

    print(f"Going to {dest}!")
