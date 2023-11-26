num = input()

sumo = 0
sumd = 0

for i in num:
    if int(i) % 2 == 0:
        sumd += int(i)
    else:
        sumo += int(i)

print(f"Odd sum = {sumo}, Even sum = {sumd}")
