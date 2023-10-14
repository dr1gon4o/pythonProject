import os

x = float(input())
x2 = input()

x3 = 0
x4 = 0
x5 = 0

if x <= 100:
    x3 = 'Bulgaria'
    if x2 == 'summer':
        x4 = x * 0.3
        x5 = 'Camp'
    elif x2 == 'winter':
        x4 = x * 0.7
        x5 = 'Hotel'

elif x <= 1000:
    x3 = 'Balkans'
    if x2 == 'summer':
        x4 = x * 0.4
        x5 = 'Camp'
    elif x2 == 'winter':
        x4 = x * 0.8
        x5 = 'Hotel'

elif x > 1000:
    x3 = 'Europe'
    x4 = x * 0.9
    x5 = 'Hotel'

print(f"Somewhere in {x3}", f"{x5} - {x4:.02f}", sep=os.linesep)
