x1 = int(input())
x2 = int(input())
x3 = int(input())

# komanda = input()

obem = x1 * x2 * x3
kashoni = 0

while True:
    komanda = input()
    if komanda == "Done":
        break
    komanda = int(komanda)
    kashoni += komanda

    if obem < kashoni:
        break

if obem >= kashoni:
    print(f"{obem - kashoni} Cubic meters left.")
else:
    print(f"No more free space! You need {kashoni - obem} Cubic meters more.")
