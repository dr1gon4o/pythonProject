import math

x = input()
area = 0

if x == 'square':
    x1 = float(input())
    area = x1 ** 2

elif x == 'rectangle':
    x1 = float(input())
    x2 = float(input())
    area = x1 * x2

elif x == 'circle':
    x1 = float(input())
    area = x1 ** 2 * math.pi

elif x == 'triangle':
    x1 = float(input())
    x2 = float(input())
    area = 1/2 * x1 * x2

print(f"{area:.3f}")
