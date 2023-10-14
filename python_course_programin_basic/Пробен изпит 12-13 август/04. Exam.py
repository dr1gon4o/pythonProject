x = int(input())

g1 = 0
g2 = 0
g3 = 0
g4 = 0
x3 = 0

for i in range(0, x):
    x2 = float(input())
    x3 += x2
    if x2 < 3:
        g1 += 1
    elif 3 <= x2 <= 3.99:
        g2 += 1
    elif 4 <= x2 <= 4.99:
        g3 += 1
    elif x2 >= 5:
        g4 += 1

g1 = (g1 / x) * 100
g2 = (g2 / x) * 100
g3 = (g3 / x) * 100
g4 = (g4 / x) * 100

average = x3 / x

print(f"Top students: {g4:.02f}%")
print(f"Between 4.00 and 4.99: {g3:.02f}%")
print(f"Between 3.00 and 3.99: {g2:.02f}%")
print(f"Fail: {g1:.02f}%")
print(f"Average: {average:.02f}")
