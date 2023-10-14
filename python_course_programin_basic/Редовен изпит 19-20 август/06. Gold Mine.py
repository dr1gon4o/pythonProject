b_lokacia = int(input())


for i in range (1, b_lokacia + 1):
    o_averag = float(input())
    dni = int(input())
    all_zlato = 0
    # avere_den = all_zlato / dni

    for j in range(1, dni + 1):
        zlato_den = float(input())
        all_zlato += zlato_den
    avere_den = all_zlato / dni
    if avere_den >= o_averag:
        print(f"Good job! Average gold per day: {avere_den:.02f}.")
    else:
        print(f"You need {o_averag - avere_den:.02f} gold.")
