dest = input()
suma = float(input())
x = 0
xx = False
while True:
    if dest == "End":
        break
    cena = float(input())
    x += cena
    if x >= suma:
        print(f"Going to {dest}!")
        xx = True
    while xx:
        x = 0
        xx = False
        dest = input()
        suma = float(input())
