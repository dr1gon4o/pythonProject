import os

broi_g = int(input())

musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
all = 0

for i in range(broi_g):
    broi_k = int(input())
    all += broi_k
    if broi_k <= 5:
        musala += broi_k
    elif 6 <= broi_k <= 12:
        monblan += broi_k
    elif 13 <= broi_k <= 25:
        kilimandjaro += broi_k
    elif 26 <= broi_k <= 40:
        k2 += broi_k
    elif broi_k >= 41:
        everest += broi_k

x1 = musala / all * 100
x2 = monblan / all * 100
x3 = kilimandjaro / all * 100
x4 = k2 / all * 100
x5 = everest / all * 100

print(f"{x1:.02f}%", f"{x2:.02f}%", f"{x3:.02f}%", f"{x4:.02f}%", f"{x5:.02f}%", sep=os.linesep)
