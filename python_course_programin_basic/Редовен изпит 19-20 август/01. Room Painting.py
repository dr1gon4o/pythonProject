import math

x1 = int(input())
x2 = int(input())
x3 = float(input())
x4 = float(input())

cx1 = x1 * 21.50
cx2 = x2 * 5.20
cx3 = x2 * 0.35
cx3 = math.ceil(cx3)
cx3 = cx3 * x3
cx4 = x1 * 0.48
cx4 = math.floor(cx4)
cx4 = cx4 * x4

all = cx4 + cx3 + cx2 + cx1
price = all / 15

print(f"This delivery will cost {price:.02f} lv.")
