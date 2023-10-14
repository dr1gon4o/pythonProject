x1 = float(input())
x2 = float(input())
x3 = float(input())
x4 = float(input())
x5 = float(input())
x6 = float(input())

x7 = (x2 * 2.60) + (x3 * 3) + (x4 * 4.10) + (x5 * 8.20) + (x6 * 2)
x8 = x2 + x3 + x4 + x5 + x6

if x8 >= 50:
    x7 = x7 - (x7 * 0.25)

x9 = x7 - (x7 * 0.10)

x10 = abs(x9 - x1)

if x9 >= x1:
    print(f"Yes! {x10:.2f} lv left.")
else:
    print(f"Not enough money! {x10:.2f} lv needed.")

