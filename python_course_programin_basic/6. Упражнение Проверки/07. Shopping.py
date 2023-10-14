b = float(input())
v = int(input())
p = int(input())
r = int(input())

c_v = v * 250
c_p = p * (c_v * 0.35)
c_r = r * (c_v * 0.1)

x = c_v + c_p + c_r

if v > p:
    x = x - (x * 0.15)

if b >= x:
    print(f"You have {b - x:.02f} leva left!")

elif x > b:
    print(f"Not enough money! You need {x - b:.02f} leva more!")
