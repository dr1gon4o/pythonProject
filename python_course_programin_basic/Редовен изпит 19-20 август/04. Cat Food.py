kotki = int(input())
# x = float(input())


malki = 0
golemi = 0
ogromni = 0

g1 = 0
g2 = 0
g3 = 0

# 1 кг храна = 12.45 лева.
for i in range(1, kotki+1):
    x = float(input())

    if 100 <= x < 200:
        g1 += 1
        malki += x
    elif 200 <= x < 300:
        g2 += 1
        golemi += x
    elif 300 <= x < 400:
        g3 += 1
        ogromni += x

kg = (malki + golemi + ogromni) / 1000
price = kg * 12.45

print(f"Group 1: {g1} cats.\n"
f"Group 2: {g2} cats.\n"
f"Group 3: {g3} cats.\n"
f"Price for food per day: {price:.02f} lv."
)
