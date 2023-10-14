ime = input()

broi_godini = 0
skusani_godini = 0
bori_ocenki = 0

while True:
    ocenka = float(input())

    if ocenka < 4:
        skusani_godini += 1
        if skusani_godini > 1:
            broi_godini += 1
            print(f'{ime} has been excluded at {broi_godini} grade')
            break
    else:
        broi_godini += 1
        bori_ocenki += ocenka
    if broi_godini == 12:
        print(f"{ime} graduated. Average grade: {bori_ocenki / 12:.2f}")
        break
