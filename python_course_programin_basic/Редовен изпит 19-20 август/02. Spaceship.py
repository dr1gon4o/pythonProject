import math

x1 = float(input())
x2 = float(input())
x3 = float(input())
x4 = float(input())



shirina = 2
duljina = 2
visochina = x4 + 0.4

obem_za1 = shirina * duljina * visochina

obem_korab = x1 * x2 * x3

obem_za3 = obem_za1 * 3
obem_za10 = obem_za1 * 10

astro = math.floor(obem_korab/obem_za1)

if obem_za3 <= obem_korab <= obem_za10:
    print(f"The spacecraft holds {astro} astronauts.")
elif obem_korab < obem_za3:
    print("The spacecraft is too small.")
elif obem_korab > obem_za10:
    print("The spacecraft is too big.")
