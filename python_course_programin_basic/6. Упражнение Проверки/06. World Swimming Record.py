import math

x1 = float(input())
x2 = float(input())
x3 = float(input())

x4 = x3 * x2
x5 = math.floor(x2 / 15) * 12.5

x6 = x4 + x5

if x6 < x1:
    print(f" Yes, he succeeded! The new world record is {abs(x6):.02f} seconds.")

else:
    print(f"No, he failed! He was {abs(x1 - x6):.02f} seconds slower.")
