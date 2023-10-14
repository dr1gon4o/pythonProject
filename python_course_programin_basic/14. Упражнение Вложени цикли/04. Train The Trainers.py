juri = int(input())
ime = input()

all_2 = 0
sum_2 = 0
popo = False

while True:
    # ime = input()
    if ime == 'Finish':
        popo = True
        break
    all = 0
    sum = 0

    for j in range(1, juri + 1):
        b_prez = float(input())
        all += 1
        all_2 += 1
        sum += b_prez
        sum_2 += b_prez
    avere = sum / all
    avere_2 = sum_2 / all_2
    print(f"{ime} - {avere:.02f}.")

    ime = input()

if popo:
    print(f"Student's final assessment is {avere_2:.02f}.")
