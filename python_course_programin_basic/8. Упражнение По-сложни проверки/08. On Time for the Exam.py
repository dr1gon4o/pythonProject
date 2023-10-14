import os

x = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())

x5 = (x * 60) + x2
x6 = (x3 * 60) + x4
diff = abs(x6 - x5)
x7 = diff // 60
x8 = diff % 60

x9: 0

if x6 > x5:
    x9 = 'Late'
    if diff >= 60:
        print(f"{x9}", f"{x7}:{x8:02d} hours after the start", sep=os.linesep)
    else:
        print(f"{x9}", f"{x8} minutes after the start", sep=os.linesep)

elif x6 == x5 or diff <= 30:
    x9 = 'On time'
    print(x9)
    if diff > 0:
        print(f"{x9}", f"{x8} minutes before the start", sep=os.linesep)

else:
    x9 = 'Early'
    if diff >= 60:
        print(f"{x9}", f"{x7}:{x8:02d} hours before the start", sep=os.linesep)
    else:
        print(f"{x9}", f"{x8} minutes before the start", sep=os.linesep)
