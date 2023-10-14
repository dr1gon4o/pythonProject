x = int(input()) * 60
x2 = int(input()) + 15
x3 = x + x2

x4 = x3 // 60
x5 = x3 % 60

if x4 > 23:
    x4 = 0

print(f"{x4}:{x5:02}")
