x = float(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
x6 = int(input())

x7 = x2 + x3 + x4 + x5 + x6

all = (x2 * 0.60) + (x3 * 7.20) + (x4 * 3.60) + (x5 * 18.20) + (x6 * 22)


if x7 >= 25:
    all = all * 0.65

razhod = all * 0.90

if razhod >= x:
    print(f"Yes! {razhod-x:.02f} lv left.")
else:
    print(f"Not enough money! {x-razhod:.02f} lv needed.")
