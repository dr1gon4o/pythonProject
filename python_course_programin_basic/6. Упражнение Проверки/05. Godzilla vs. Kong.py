x1 = float(input())
x2 = int(input())
x3 = float(input())

x4 = x1 * 0.1
x5 = x2 * x3

if x2 > 150:
    x5 = x5 - (x5 * 0.1)

if x4 + x5 > x1:
    print("Not enough money!")
    print(f"Wingard needs {(x4 + x5) - x1:.02f} leva more.")

else:
    print("Action!")
    print(f"Wingard starts filming with {x1 - (x4 +x5):.02f} leva left.")
