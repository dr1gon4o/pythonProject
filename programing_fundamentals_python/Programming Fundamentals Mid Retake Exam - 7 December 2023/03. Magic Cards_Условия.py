line = input().split(":")
line2 = input()

haha = []

while line2 != "Ready":

    hoho = line2.split()

    if hoho[0] == "Add":
        if hoho[1] in line:
            haha.append(hoho[1])
        else:
            print("Card not found.")
    if hoho[0] == "Insert":
        if hoho[1] in line and 0 <= int(hoho[2]) <= len(haha):
            haha.insert(int(hoho[2]), hoho[1])
        else:
            print("Error!")
    if hoho[0] == "Remove":
        if hoho[1] in haha:
            haha.remove(hoho[1])
        else:
            print("Card not found.")
    if hoho[0] == "Swap":
        tempIndex = haha.index(hoho[1])
        tempIndex2 = haha.index(hoho[2])
        haha[tempIndex], haha[tempIndex2] = haha[tempIndex2], haha[tempIndex]
    if hoho[0] == "Shuffle":
        haha.reverse()

    # print("line2")
    line2 = input()
    # line = input().split(":")


# print(line)
# print(line2)
# print(hoho)
# print(haha.reverse())
print(*haha, sep=" ")