n = int(input())
# x = float(input())
# x2 = float(input())

x3 = 0
x4 = 0

for i in range(1, n + 1):
    x = float(input())
    x2 = float(input())
    x3 += x
    x4 += x * x2
x5 = x4 / x3

print(f"Liter: {x3:.02f}")
print(f"Degrees: {x5:.02f}")

if x5 < 38:
    print("Not good, you should baking!")
elif 38 <= x5 <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")