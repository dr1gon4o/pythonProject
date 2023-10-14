minuti = int(input())
razxodka = int(input())
kalori = int(input())

ob_minut = minuti * razxodka
ob_kal = ob_minut * 5

if ob_kal >= (kalori / 2):
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {ob_kal}." )

else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {ob_kal}.")
