tab = int(input())
zap = int(input())

for i in range(tab):
    n = input()
    if n == 'Facebook':
        zap = zap - 150
    elif n == 'Instagram':
        zap = zap - 100
    elif n == 'Reddit':
        zap = zap - 50
    if zap <= 0:
        print("You have lost your salary.")
        break
else:
    print(zap)
