d = int(input())
sh = int(input())

obem = d * sh
parcheta = 0

while True:
    komand = input()
    if komand == 'STOP':
        break
    komand = int(komand)
    # obem -= komand
    parcheta += komand

    if parcheta >= obem:
        break

if parcheta >= obem:
    print(f"No more cake left! You need {parcheta - obem} pieces more.")
else:
    print(f"{obem-parcheta} pieces are left.")

