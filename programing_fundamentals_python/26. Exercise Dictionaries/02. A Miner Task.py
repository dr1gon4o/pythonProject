line = input()

haha = []

while line != "stop":
    haha.append(line)
    line = input()

haha2 = {}
for x in range(0, len(haha), 2):
    key = haha[x]
    value = haha[x + 1]

    if key not in haha2:
        haha2[key] = int(value)
    else:
        haha2[key] += int(value)

for x,i in haha2.items():
    print(f"{x} -> {i}")


# print(haha)
# print(haha2)