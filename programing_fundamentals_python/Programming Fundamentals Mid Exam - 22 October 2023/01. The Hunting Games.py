days_adventure = int(input())
count_players = int(input())
group_energy = float(input())
water_perday = float(input())
food_perday = float(input())

all_water = days_adventure * count_players * water_perday
all_food = days_adventure * count_players * food_perday
current_energy = group_energy

for current_day in range(1, days_adventure +1):
    energy_lost = float(input())
    current_energy -= energy_lost
    if current_day % 2 == 0:
        current_energy = current_energy + (current_energy * 0.05)
        all_water = all_water * 0.7
    if current_day % 3 == 0:
        current_energy = current_energy + (current_energy * 0.1)
        all_food = all_food - (all_food / count_players)

    if current_energy <= 0:
        break

if current_energy > 0:
    print(f"You are ready for the quest. You will be left with - {current_energy:.02f} energy!")
else:
    print(f"You will run out of energy. You will be left with {all_food:.02f} food and {all_water:.02f} water.")
