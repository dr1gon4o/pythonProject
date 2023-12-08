# line = input().split("-")
# num = int(input())
# name = input()

# haha = {k: x for k, x in input().split("-")}
haha = {}

while True:
    line = input()
    if "-" not in line:
        break
    k, v = line.split("-")
    haha[k] = v


# for x in range(0, len(line), 2):
#     k = line[x]
#     v = line[x +1]
#     haha[k] = v

# num = int(input())
for x in range(int(line)):
    name = input()
    if name in haha.keys():
        print(f"{name} -> {haha.get(name)}")
    else:
        print(f"Contact {name} does not exist.")

# print(line)
# print(haha)