import math

name = input()
ep = int(input())
po = int(input())

v_ob = po /8
v_ot = po /4

iz_v = v_ob + v_ot
o_v = po - iz_v
n_v = abs(po - (iz_v + ep))

if o_v >= ep:
    print(f"You have enough time to watch {name} and left with {math.ceil(o_v - ep)} minutes free time.")

else:
    print(f"You don't have enough time to watch {name}, you need {math.ceil(n_v)} more minutes.")
