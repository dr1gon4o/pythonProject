import sys

x = input()

x2 = -sys.maxsize

while x != 'Stop':
    x3 = int(x)

    if x3 > x2:
        x2 = x3
    x = input()

print(x2)
