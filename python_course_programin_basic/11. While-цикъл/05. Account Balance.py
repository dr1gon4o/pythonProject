x = input()
x2 = 0

while x != "NoMoreMoney":
    x3 = float(x)

    if x3 < 0:
        print("Invalid operation!")
        break

    x2 += x3
    print(f"Increase: {x3:.2f}")
    x = input()

print(f"Total: {x2:.2f}")
