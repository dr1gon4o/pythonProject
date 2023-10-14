n = int(input())
peralnia = float(input())
toy = int(input())

bonus = 0
suma = 0
suma2 = 0

for i in range(1, n + 1):
        if i % 2 == 0:
            bonus += 10
            suma += bonus - 1
        else:
            suma2 += toy

all = suma2 + suma

if all >= peralnia:
    print(f"Yes! {all - peralnia:.02f}")
else:
    print(f"No! {peralnia - all:.02f}")
