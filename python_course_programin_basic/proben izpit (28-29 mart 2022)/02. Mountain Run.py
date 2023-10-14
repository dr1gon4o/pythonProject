import math

rekord = float(input())
metri = float(input())
vreme = float(input())

nu_vreme = metri * vreme
vreme_ivan = math.floor(metri / 50) * 30 + nu_vreme

if vreme_ivan < rekord:
    print(f" Yes! The new record is {vreme_ivan:.02f} seconds.")
else:
    print(f"No! He was {vreme_ivan - rekord:.02f} seconds slower.")
