pari_eks = float(input())
pari_na = float(input())


broi_dni = 0
broi_dni_2 = 0
all_suma = pari_na

while True:
    text = input()
    suma = float(input())
    broi_dni += 1

    if text == 'spend':
        broi_dni_2 += 1
        if suma > all_suma:
            all_suma = 0
        else:
            all_suma -= suma

    if text == 'save':
        all_suma += suma
        broi_dni_2 = 0

    if broi_dni_2 >= 5:
        print(f"You can't save the money.\n{broi_dni}")
        break
    if all_suma >= pari_eks:
        print(f"You saved the money for {broi_dni} days.")
        break
