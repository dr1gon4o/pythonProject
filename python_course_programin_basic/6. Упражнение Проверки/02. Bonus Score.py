x = int(input())
x2 = 0

if x <= 100:
    x2 = 5

elif 100 < x <= 1000:
    x2 = x * 0.20

elif x > 1000:
    x2 = x * 0.10

if x % 2 == 0:
    print(x2 + 1)
    print(x + x2 + 1)

elif x % 5 == 0:
    print(x2 + 2)
    print(x + x2 + 2)

else:
    print(x2)
    print(x + x2)
