import math

x1 = int(input())
x2 = int(input())
x3 = float(input())
x4 = float(input())

cx1 = x1 * 13
cx2 = x2 * 13

cx33 = cx1 + cx2 + 1000
cx3 = x4 - x3

cx4 = 13 * cx3

cx5 = math.ceil(cx33 / cx4)

print(f"{cx33}\n "
      f"{cx5} ")
