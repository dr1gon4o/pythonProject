x = int(input())
x2 = int(input())
x3 = int(input())
x4 = x + x2 + x3

x5 = x4 // 60
x6 = x4 % 60

if x4 == 60:
    print(f"{x5}:{0:02d}")

elif x4 < 60:
    print(f"{00}:{x4:02d}")

else:
    print(f"{x5}:{x6:02d}")
