
hoho = {"shards": 0, "fragments": 0, "motes": 0}
line = input().split()


flag = False
while not flag:
    for x in range(0, len(line), 2):
        k = line[x + 1].lower()
        v = int(line[x])
        if k not in hoho.keys():
            hoho[k] = 0
        hoho[k] += v
        if hoho["shards"] >= 250:
            print("Shadowmourne obtained!")
            hoho["shards"] -= 250
            flag = True
        elif hoho["fragments"] >= 250:
            print("Valanyr obtained!")
            hoho["fragments"] -= 250
            flag = True
        elif hoho["motes"] >= 250:
            print("Dragonwrath obtained!")
            hoho["motes"] -= 250
            flag = True
        if flag:
            break
    if flag:
        break

    line = input().split()

for k, v in hoho.items():
    print(f"{k}: {v}")


# print(line)
# print(haha)
# print(hoho)
