import math
import os

tur = int(input())
toch_n = int(input())

toch = toch_n
pr = 0

for i in range(tur):
    x = input()
    if x == 'W':
        toch += 2000
        pr += 1
    elif x == 'F':
        toch += 1200
    elif x == 'SF':
        toch += 720

sre = math.floor((toch - toch_n) / tur)
pr = pr / tur * 100

print(f"Final points: {toch}", f"Average points: {sre}", f"{pr:.02f}%", sep=os.linesep)
