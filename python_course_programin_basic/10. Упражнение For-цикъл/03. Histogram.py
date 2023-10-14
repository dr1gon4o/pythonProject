import os

n = int(input())

# p1 < 200
# 200 < p2 < 399
# 400 < p3 < 599
# 600 < p4 < 799
# p5 >= 800
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(0, n):
    x = int(input())
    if x < 200:
        p1 += 1
    elif 200 <= x <= 399:
        p2 += 1
    elif 400 <= x <= 599:
        p3 += 1
    elif 600 <= x <= 799:
        p4 += 1
    elif x >= 800:
        p5 += 1

p1 = p1 / n * 100
p2 = p2 / n * 100
p3 = p3 / n * 100
p4 = p4 / n * 100
p5 = p5 / n * 100

print(f"{p1:.02f}%", f"{p2:.02f}%", f"{p3:.02f}%", f"{p4:.02f}%", f"{p5:.02f}%", sep=os.linesep)
